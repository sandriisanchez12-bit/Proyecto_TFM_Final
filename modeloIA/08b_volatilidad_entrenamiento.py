"""
08b_volatilidad_entrenamiento.py
-----------------------------------
Entrenamiento XGBoost para predecir régimen de volatilidad futura (h=10d).
Hiperparámetros conservadores dado el tamaño de muestra tras la purga (~818 filas).
Optuna optimiza ROC-AUC (más informativo que accuracy para este problema).
"""

import os
import json
import numpy as np
import xgboost as xgb
import optuna
from optuna.samplers import TPESampler
from sklearn.metrics import accuracy_score, roc_auc_score
import warnings
warnings.filterwarnings("ignore")
optuna.logging.set_verbosity(optuna.logging.WARNING)

FEATURE_DIR = "./data/features_vol"
MODEL_DIR   = "./models_vol"
RESULTS_DIR = "./results_vol"
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

N_TRIALS   = 600
EARLY_STOP = 50
USE_GPU    = False


def load_data():
    def load(split):
        X = np.load(os.path.join(FEATURE_DIR, f"X_{split}.npy"))
        y = np.load(os.path.join(FEATURE_DIR, f"y_{split}.npy"))
        return X, y
    return load("train"), load("val"), load("test")


def objective(trial, X_train, y_train, X_val, y_val, device):
    params = {
        "objective":         "binary:logistic",
        "eval_metric":       "auc",
        "tree_method":       "hist",
        "device":            device,
        "seed":              42,
        "learning_rate":     trial.suggest_float("learning_rate", 0.005, 0.1, log=True),
        "max_depth":         trial.suggest_int("max_depth", 2, 5),
        "min_child_weight":  trial.suggest_int("min_child_weight", 10, 50),
        "subsample":         trial.suggest_float("subsample", 0.5, 0.9),
        "colsample_bytree":  trial.suggest_float("colsample_bytree", 0.3, 0.8),
        "colsample_bylevel": trial.suggest_float("colsample_bylevel", 0.3, 0.8),
        "gamma":             trial.suggest_float("gamma", 0.1, 5.0),
        "lambda":            trial.suggest_float("lambda", 0.5, 20.0, log=True),
        "alpha":             trial.suggest_float("alpha", 0.05, 10.0, log=True),
    }
    n_estimators = trial.suggest_int("n_estimators", 50, 800)

    dtrain = xgb.DMatrix(X_train, label=y_train)
    dval   = xgb.DMatrix(X_val,   label=y_val)

    model = xgb.train(
        params, dtrain,
        num_boost_round       = n_estimators,
        evals                 = [(dval, "val")],
        early_stopping_rounds = EARLY_STOP,
        verbose_eval          = False,
    )

    probs = model.predict(dval)
    auc   = roc_auc_score(y_val, probs)

    best_acc, best_thr = 0, 0.5
    for thr in np.arange(0.30, 0.71, 0.01):
        preds = (probs >= thr).astype(int)
        if len(np.unique(preds)) < 2:
            continue
        acc = accuracy_score(y_val, preds)
        if acc > best_acc:
            best_acc, best_thr = acc, thr

    trial.set_user_attr("threshold", best_thr)
    trial.set_user_attr("val_acc", best_acc)
    return auc


def train_final(best_params, X_train, y_train, X_val, y_val, device):
    n_estimators = best_params.pop("n_estimators")
    params = {
        "objective":   "binary:logistic",
        "eval_metric": ["auc", "logloss"],
        "tree_method": "hist",
        "device":      device,
        "seed":        42,
        **best_params,
    }
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dval   = xgb.DMatrix(X_val,   label=y_val)

    model = xgb.train(
        params, dtrain,
        num_boost_round       = n_estimators * 2,
        evals                 = [(dtrain, "train"), (dval, "val")],
        early_stopping_rounds = EARLY_STOP * 2,
        verbose_eval          = 50,
    )
    return model


if __name__ == "__main__":
    print("Cargando features...")
    (X_train, y_train), (X_val, y_val), (X_test, y_test) = load_data()
    print(f"  Train: {X_train.shape} | Val: {X_val.shape} | Test: {X_test.shape}")
    print(f"  Alta vol — train: {y_train.mean()*100:.1f}%  val: {y_val.mean()*100:.1f}%  test: {y_test.mean()*100:.1f}%")

    device = "cuda" if USE_GPU else "cpu"
    print(f"  Dispositivo: {device}")

    print(f"\nOptimizando con Optuna ({N_TRIALS} trials, objetivo=ROC-AUC)...")
    study = optuna.create_study(direction="maximize", sampler=TPESampler(seed=42))
    study.optimize(
        lambda t: objective(t, X_train, y_train, X_val, y_val, device),
        n_trials=N_TRIALS, show_progress_bar=True, gc_after_trial=True,
    )

    best_auc       = study.best_value
    best_params    = study.best_params.copy()
    best_threshold = study.best_trial.user_attrs.get("threshold", 0.5)
    best_val_acc   = study.best_trial.user_attrs.get("val_acc", 0.0)

    print(f"\nMejor ROC-AUC val : {best_auc:.4f}")
    print(f"DirAcc val        : {best_val_acc*100:.2f}%")
    print(f"Threshold óptimo  : {best_threshold:.2f}")

    study.trials_dataframe().to_csv(
        os.path.join(RESULTS_DIR, "optuna_trials.csv"), index=False)

    print("\nEntrenando modelo final...")
    final_model = train_final(best_params.copy(), X_train, y_train, X_val, y_val, device)

    probs_val = final_model.predict(xgb.DMatrix(X_val))
    auc_val   = roc_auc_score(y_val, probs_val)
    preds_val = (probs_val >= best_threshold).astype(int)
    print(f"  ROC-AUC val final : {auc_val:.4f}")
    print(f"  DirAcc val final  : {accuracy_score(y_val, preds_val)*100:.2f}%")

    final_model.save_model(os.path.join(MODEL_DIR, "xgb_model.json"))
    params_save = best_params.copy()
    params_save["best_auc"]   = best_auc
    params_save["threshold"]  = best_threshold
    with open(os.path.join(MODEL_DIR, "xgb_best_params.json"), "w") as f:
        json.dump(params_save, f, indent=2)

    print(f"\nModelo guardado. Siguiente paso: python 08c_volatilidad_testeo.py")
