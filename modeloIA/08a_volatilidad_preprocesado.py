"""
08a_volatilidad_preprocesado.py
----------------------------------
NUEVO TARGET: régimen de volatilidad futura del SP500 (h=10 días)
  Clase 1 = volatilidad futura (std de retornos en los próximos 10 días)
            por ENCIMA de la mediana histórica  -> "régimen de alta volatilidad"
  Clase 0 = volatilidad futura por debajo de la mediana -> "régimen tranquilo"

Por qué este target y no dirección de precio:
  - Validado con Purged TimeSeriesSplit: ROC-AUC ~0.81 vs ~0.49 de dirección
  - El "volatility clustering" es uno de los efectos más robustos y replicados
    en series financieras (efecto ARCH/GARCH) -> hay señal real explotable
  - Tiene aplicación práctica directa: gestión de riesgo, position sizing,
    hedging con opciones, ajuste de exposición de cartera

Variables: SP500, Oro, Plata, Cobre, Petróleo WTI, Gas Natural, VIX, Dólar
Rango: 2000-08-31 a 2025-12-31
"""

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# ---------------------------------------------------------------
# RUTAS — ajusta si es necesario
# ---------------------------------------------------------------
TRAIN_CSV = r"C:\Users\usuario\Desktop\tfm_sandra\xgboost\train_2000_vix_usd_v2.csv"
VAL_CSV   = r"C:\Users\usuario\Desktop\tfm_sandra\xgboost\val_2000_vix_usd_v2.csv"
TEST_CSV  = r"C:\Users\usuario\Desktop\tfm_sandra\xgboost\test_2000_vix_usd_v2.csv"

FEATURE_DIR = "./data/features_vol"
MODEL_DIR   = "./models_vol"
os.makedirs(FEATURE_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

TARGET_ASSET = "SP500_logret"
HORIZON      = 10          # horizonte con mejor ROC-AUC en el diagnóstico
PURGE_STEP   = 1           # submuestreo en train/val para reducir solapamiento

ASSETS = [
    "SP500_logret",
    "Oro_logret",
    "GasNatural_logret",
    "Plata_logret",
    "Cobre_logret",
    "PetroleoWTI_logret",
    "VIX_logret",
    "Dolar_logret",
]

LAGS       = list(range(1, 21))         # lags completos para SP500
LAGS_OTROS = [1, 2, 3, 5, 10, 15, 20]   # lags reducidos para el resto


def load_returns():
    train = pd.read_csv(TRAIN_CSV, index_col=0, parse_dates=True)
    val   = pd.read_csv(VAL_CSV,   index_col=0, parse_dates=True)
    test  = pd.read_csv(TEST_CSV,  index_col=0, parse_dates=True)
    df    = pd.concat([train, val, test]).sort_index()

    cols    = [c for c in ASSETS if c in df.columns]
    missing = [c for c in ASSETS if c not in df.columns]
    if missing:
        print(f"  AVISO columnas no encontradas: {missing}")

    if "VIX_nivel" in df.columns:
        return df[cols + ["VIX_nivel"]].dropna()
    return df[cols].dropna()


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    series = {}
    asset_cols = [c for c in df.columns if c != "VIX_nivel"]

    # Lags de retornos
    for col in asset_cols:
        lags_usar = LAGS if col == TARGET_ASSET else LAGS_OTROS
        for lag in lags_usar:
            series[f"{col}_lag{lag}"] = df[col].shift(lag)

    sp = df[TARGET_ASSET].shift(1)

    # Volatilidad rolling SP500 (features de entrada — info pasada)
    for w in [5, 10, 20, 60]:
        series[f"SP500_vol{w}"] = sp.rolling(w).std()
    series["SP500_vol_ratio_5_20"]  = sp.rolling(5).std()  / (sp.rolling(20).std() + 1e-8)
    series["SP500_vol_ratio_10_60"] = sp.rolling(10).std() / (sp.rolling(60).std() + 1e-8)

    # Momentum
    for w in [5, 10, 20]:
        series[f"SP500_mom{w}"] = sp.rolling(w).sum()

    # RSI
    for w in [14, 28]:
        gain = sp.clip(lower=0).rolling(w).mean()
        loss = (-sp.clip(upper=0)).rolling(w).mean()
        series[f"SP500_rsi{w}"] = 100 - (100 / (1 + gain / (loss + 1e-8)))

    # MACD
    ema12 = sp.ewm(span=12, adjust=False).mean()
    ema26 = sp.ewm(span=26, adjust=False).mean()
    macd  = ema12 - ema26
    series["SP500_macd"]      = macd
    series["SP500_macd_hist"] = macd - macd.ewm(span=9, adjust=False).mean()

    # Bandas de Bollinger
    bb_mean = sp.rolling(20).mean()
    bb_std  = sp.rolling(20).std()
    series["SP500_bb_pct"] = (sp - bb_mean) / (2 * bb_std + 1e-8)

    # Régimen de mercado
    ema50  = sp.ewm(span=50,  adjust=False).mean()
    ema200 = sp.ewm(span=200, adjust=False).mean()
    series["SP500_tendencia"]    = ema50 - ema200
    series["SP500_sobre_ema200"] = sp - ema200
    series["SP500_zscore20"] = (sp - sp.rolling(20).mean()) / (sp.rolling(20).std() + 1e-8)
    series["SP500_zscore60"] = (sp - sp.rolling(60).mean()) / (sp.rolling(60).std() + 1e-8)

    # ── Features del VIX — las más importantes para este target ────
    if "VIX_nivel" in df.columns:
        vix = df["VIX_nivel"].shift(1)
        series["VIX_nivel"]         = vix
        series["VIX_zscore60"]      = (vix - vix.rolling(60).mean()) / (vix.rolling(60).std() + 1e-8)
        series["VIX_percentil"]     = vix.rolling(252).rank(pct=True)
        series["VIX_sobre_media20"] = vix - vix.rolling(20).mean()
        series["VIX_panico"]        = (vix > 30).astype(float)
        series["VIX_tendencia"]     = vix.diff(5)   # variación reciente del VIX

    # Correlaciones rolling
    if "Oro_logret" in df.columns:
        series["corr_sp500_oro30"] = df[TARGET_ASSET].shift(1).rolling(30).corr(df["Oro_logret"].shift(1))
    if "VIX_logret" in df.columns:
        series["corr_sp500_vix30"] = df[TARGET_ASSET].shift(1).rolling(30).corr(df["VIX_logret"].shift(1))

    # Calendario
    series["dia_semana"] = pd.Series(df.index.dayofweek, index=df.index).astype(float)
    series["mes"]        = pd.Series(df.index.month,     index=df.index).astype(float)

    # ── TARGET: régimen de volatilidad futura ───────────────────────
    vol_futura = df[TARGET_ASSET].rolling(HORIZON).std().shift(-HORIZON)
    feat_temp  = pd.DataFrame(series, index=df.index)
    vol_mediana = vol_futura.median()  # mediana global (calculada después se recalibra solo con train)
    series["vol_futura"] = vol_futura  # guardamos el valor continuo también, útil para análisis

    feat = pd.DataFrame(series, index=df.index).dropna()
    return feat


def split_normalize_save(feat: pd.DataFrame):
    train_idx = pd.read_csv(TRAIN_CSV, index_col=0, parse_dates=True).index
    val_idx   = pd.read_csv(VAL_CSV,   index_col=0, parse_dates=True).index
    test_idx  = pd.read_csv(TEST_CSV,  index_col=0, parse_dates=True).index

    train = feat[feat.index.isin(train_idx)]
    val   = feat[feat.index.isin(val_idx)]
    test  = feat[feat.index.isin(test_idx)]

    # La mediana de volatilidad se calcula SOLO con train (evita leakage)
    # vol_mediana_train = train["vol_futura"].median()
    # print(f"  Mediana de volatilidad futura (train): {vol_mediana_train:.5f}")

    for name, subset in [("train", train), ("val", val), ("test", test)]:
        subset = subset.copy()

    # Umbral de alta volatilidad: percentil 70 SOLO con train
    threshold_vol = train["vol_futura"].quantile(0.70)

    print(f"  Umbral alta volatilidad P70 (train): {threshold_vol:.5f}")

    def make_target(subset):
        return (subset["vol_futura"] > threshold_vol).astype(int)

    y_train = make_target(train).values.astype(np.int32)
    y_val   = make_target(val).values.astype(np.int32)
    y_test  = make_target(test).values.astype(np.int32)

    feat_cols = [c for c in feat.columns if c != "vol_futura"]

    X_train = train[feat_cols].values.astype(np.float32)
    X_val   = val[feat_cols].values.astype(np.float32)
    X_test  = test[feat_cols].values.astype(np.float32)

    # ── Purga de solapamiento (igual que en el pipeline de dirección) ──
    X_train = X_train[::PURGE_STEP]
    y_train = y_train[::PURGE_STEP]
    X_val   = X_val[::PURGE_STEP]
    y_val   = y_val[::PURGE_STEP]
    print(f"  (Purga aplicada: muestreo cada {PURGE_STEP} días en train/val)")

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train).astype(np.float32)
    X_val   = scaler.transform(X_val).astype(np.float32)
    X_test  = scaler.transform(X_test).astype(np.float32)

    for split, X, y in [("train", X_train, y_train),
                         ("val",   X_val,   y_val),
                         ("test",  X_test,  y_test)]:
        np.save(os.path.join(FEATURE_DIR, f"X_{split}.npy"), X)
        np.save(os.path.join(FEATURE_DIR, f"y_{split}.npy"), y)
        print(f"  {split}: X={X.shape} | alta_vol={y.mean()*100:.1f}% baja_vol={(1-y.mean())*100:.1f}%")

    joblib.dump(scaler, os.path.join(MODEL_DIR, "scaler.pkl"))
    pd.Series(feat_cols).to_csv(os.path.join(FEATURE_DIR, "feature_names.csv"), index=False)

    with open(os.path.join(MODEL_DIR, "vol_mediana_train.txt"), "w") as f:
        f.write(str(threshold_vol))

    print(f"\n  Total features: {len(feat_cols)}")


if __name__ == "__main__":
    print("Cargando datos 2000-2025 (con VIX y Dólar)...")
    df = load_returns()
    print(f"Activos  : {list(df.columns)}")
    print(f"Rango    : {df.index.min().date()} → {df.index.max().date()}")

    print(f"\nConstruyendo features (target: régimen de volatilidad h={HORIZON}d)...")
    feat = build_features(df)

    print("\nSplit, target y normalización...")
    split_normalize_save(feat)

    print(f"\nPreprocesado completado.")
    print(f"Siguiente paso: python 08b_volatilidad_entrenamiento.py")
