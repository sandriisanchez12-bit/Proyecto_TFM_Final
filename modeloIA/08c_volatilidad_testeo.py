"""
08c_volatilidad_testeo.py
----------------------------
Evaluación del modelo de régimen de volatilidad sobre TEST.

Genera:
  - DirAcc, ROC-AUC, F1-macro, reporte de clasificación
  - Test de significancia estadística
  - Curva ROC, matriz de confusión, importancia de features
  - Interpretación: aplicación práctica para gestión de riesgo
"""

import os
import json
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import (accuracy_score, classification_report,
                              roc_auc_score, roc_curve, f1_score,
                              confusion_matrix, ConfusionMatrixDisplay)
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

FEATURE_DIR = "./data/features_vol"
MODEL_DIR   = "./models_vol"
RESULTS_DIR = "./results_vol"
os.makedirs(RESULTS_DIR, exist_ok=True)

HORIZON = 10


def load_split(split):
    X = np.load(os.path.join(FEATURE_DIR, f"X_{split}.npy"))
    y = np.load(os.path.join(FEATURE_DIR, f"y_{split}.npy"))
    return X, y


def find_best_threshold(probs, labels):
    results = []
    for thr in np.arange(0.20, 0.81, 0.01):
        preds = (probs >= thr).astype(int)
        if len(np.unique(preds)) < 2:
            continue
        acc = accuracy_score(labels, preds)
        results.append((thr, acc))
    results.sort(key=lambda x: x[1], reverse=True)
    best_thr, best_acc = results[0]
    print(f"  Threshold óptimo: {best_thr:.2f} → DirAcc val: {best_acc*100:.2f}%")
    return best_thr


def plot_roc(probs, y_true):
    try:
        import matplotlib.pyplot as plt
        fpr, tpr, _ = roc_curve(y_true, probs)
        auc = roc_auc_score(y_true, probs)
        plt.figure(figsize=(6, 5))
        plt.plot(fpr, tpr, color="#1D9E75", lw=2, label=f"XGBoost (AUC={auc:.3f})")
        plt.plot([0,1],[0,1],"k--", label="Azar")
        plt.xlabel("FPR"); plt.ylabel("TPR")
        plt.title(f"Curva ROC — Régimen volatilidad h={HORIZON}d")
        plt.legend(loc="lower right"); plt.tight_layout()
        path = os.path.join(RESULTS_DIR, "roc.png")
        plt.savefig(path, dpi=150); plt.close()
        print(f"  ROC: {path}  AUC={auc:.3f}")
        return auc
    except Exception as e:
        print(f"  (ROC no guardada: {e})"); return None


def plot_feature_importance(model, top_n=25):
    try:
        import matplotlib.pyplot as plt
        feat_names = pd.read_csv(
            os.path.join(FEATURE_DIR, "feature_names.csv"), header=None)[0].tolist()
        scores = model.get_score(importance_type="gain")
        sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
        names = []
        for k, _ in sorted_items:
            if k.startswith("f") and k[1:].isdigit():
                idx = int(k[1:])
                names.append(feat_names[idx] if idx < len(feat_names) else k)
            else:
                names.append(k)
        values = [v for _, v in sorted_items]
        fig, ax = plt.subplots(figsize=(9, 7))
        ax.barh(names[::-1], values[::-1], color="#1D9E75")
        ax.set_title(f"Top {top_n} features — Régimen de volatilidad")
        ax.set_xlabel("Ganancia (gain)"); plt.tight_layout()
        path = os.path.join(RESULTS_DIR, "feature_importance.png")
        plt.savefig(path, dpi=150); plt.close()
        print(f"  Importancia: {path}")
    except Exception as e:
        print(f"  (importancia no guardada: {e})")


def plot_confusion(y_true, preds):
    try:
        import matplotlib.pyplot as plt
        cm = confusion_matrix(y_true, preds)
        fig, ax = plt.subplots(figsize=(5, 4))
        ConfusionMatrixDisplay(cm, display_labels=["Vol. baja","Vol. alta"]).plot(
            ax=ax, colorbar=False, cmap="Greens")
        ax.set_title(f"Matriz de confusión — Régimen volatilidad h={HORIZON}d")
        plt.tight_layout()
        path = os.path.join(RESULTS_DIR, "confusion_matrix.png")
        plt.savefig(path, dpi=150); plt.close()
        print(f"  Confusión: {path}")
    except Exception as e:
        print(f"  (confusión no guardada: {e})")


if __name__ == "__main__":
    print("Cargando modelo...")
    model = xgb.Booster()
    model.load_model(os.path.join(MODEL_DIR, "xgb_model.json"))

    with open(os.path.join(MODEL_DIR, "xgb_best_params.json")) as f:
        best_params = json.load(f)
    print(f"  ROC-AUC val (Optuna): {best_params.get('best_auc', 'N/A')}")

    print("\nBuscando threshold óptimo en validación...")
    X_val, y_val = load_split("val")
    probs_val    = model.predict(xgb.DMatrix(X_val))
    threshold    = find_best_threshold(probs_val, y_val)

    print("\nEvaluando en TEST...")
    X_test, y_test = load_split("test")
    probs  = model.predict(xgb.DMatrix(X_test))
    preds  = (probs >= threshold).astype(int)

    acc      = accuracy_score(y_test, preds) * 100
    f1_macro = f1_score(y_test, preds, average="macro")
    auc      = plot_roc(probs, y_test)
    p_value  = stats.binomtest(
        int(round(acc/100 * len(y_test))), len(y_test),
        p=0.5, alternative="greater").pvalue

    print(f"\n{'='*55}")
    print(f"RESULTADOS — Régimen de volatilidad h={HORIZON}d")
    print(f"{'='*55}")
    print(f"  DirAcc XGBoost  : {acc:.2f}%")
    print(f"  ROC-AUC         : {auc:.3f}")
    print(f"  F1-macro        : {f1_macro:.4f}")
    print(f"  p-value (>50%)  : {p_value:.4f}  "
          f"{'✓ significativo' if p_value < 0.05 else '✗ no significativo'}")
    print(f"  Threshold usado : {threshold:.2f}")
    print(f"\n  Distribución test — alta vol: {y_test.mean()*100:.1f}%  baja vol: {(1-y_test.mean())*100:.1f}%")

    print(f"\nReporte detallado:")
    print(classification_report(y_test, preds, target_names=["Vol. baja", "Vol. alta"]))

    plot_feature_importance(model)
    plot_confusion(y_test, preds)

    pd.DataFrame({
        "y_true": y_test, "y_pred": preds, "prob_alta_vol": probs
    }).to_csv(os.path.join(RESULTS_DIR, "predicciones_test.csv"), index=False)

    pd.DataFrame([{
        "modelo": "XGBoost - Régimen Volatilidad", "horizonte": HORIZON,
        "n_test": len(y_test), "DirAcc": round(acc, 2),
        "F1_macro": round(f1_macro, 4), "ROC_AUC": round(auc, 3),
        "p_value": round(p_value, 4), "significativo": p_value < 0.05,
        "threshold": round(threshold, 2),
    }]).to_csv(os.path.join(RESULTS_DIR, "resumen.csv"), index=False)

    print(f"\n{'='*55}")
    print("INTERPRETACIÓN PARA EL TFM:")
    print(f"{'='*55}")
    print("""
  Este modelo NO predice la dirección del SP500, sino si el mercado
  va a entrar en un régimen de volatilidad alta o baja en los próximos
  10 días. Esto es consistente con el efecto de "volatility clustering"
  (ARCH/GARCH), uno de los fenómenos más robustos en series financieras.

  Aplicación práctica:
  - Gestión de riesgo: ajustar el tamaño de posiciones antes de periodos
    de alta volatilidad esperada
  - Estrategias de cobertura: comprar protección (opciones put, VIX
    futures) cuando el modelo anticipa alta volatilidad
  - Position sizing dinámico: reducir exposición en régimen de alta vol
    predicha, aumentar en régimen de baja vol predicha
    """)

    print(f"Resultados guardados en: {RESULTS_DIR}")
