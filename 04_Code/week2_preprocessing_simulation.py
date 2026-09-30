import pandas as pd
from sklearn.preprocessing import StandardScaler

# Synthetic example modeled on public agricultural data schemas.
df = pd.read_csv("crop_production_raw_simulated.csv")
df.columns = df.columns.str.strip().str.lower()
df["crop"] = df["crop"].astype(str).str.strip().str.title()
df = df.drop_duplicates(subset=["year","state","district","season","crop"])

# Deterministic derivation when area and reported yield exist
df["production_tonnes"] = df["production_tonnes"].fillna(
    df["area_ha"] * df["reported_yield_kg_ha"] / 1000
)

df["yield_t_ha"] = df["production_tonnes"] / df["area_ha"]

# Outlier flag — detection only
q1, q3 = df["production_tonnes"].quantile([.25, .75])
iqr = q3 - q1
df["production_outlier_flag"] = (
    (df["production_tonnes"] < q1 - 1.5*iqr) |
    (df["production_tonnes"] > q3 + 1.5*iqr)
)

# In a real ML project, fit the scaler on TRAINING data only.
scaler = StandardScaler()
df["yield_standardized"] = scaler.fit_transform(df[["yield_t_ha"]])

df.to_csv("crop_production_cleaned.csv", index=False)
