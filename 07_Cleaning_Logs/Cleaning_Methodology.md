# Cleaning Methodology

1. Profile each dataset before changing it.
2. Standardize column names, dates, numeric types and categorical labels.
3. Define natural keys and remove confirmed duplicate rows.
4. Investigate missing values by cause; do not automatically replace missing with zero.
5. Apply deterministic derivation only when the source definition supports it.
6. Use median imputation only as a documented simulation method; real project data should be source-validated first.
7. Detect outliers using IQR/z-score plus domain logic.
8. Flag suspicious values rather than automatically deleting them.
9. Standardize units and create derived features such as yield and price spread.
10. Validate logical constraints and preserve a transformation log.
11. Join datasets only after time/geography keys have compatible types and granularity.
12. For ML, fit scalers and imputers on training data only to avoid leakage.
