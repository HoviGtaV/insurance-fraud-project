from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from catboost import CatBoostClassifier

out_dir = Path("submission/monitoring")
out_dir.mkdir(parents=True, exist_ok=True)

valid_df = pd.read_parquet("data/processed/valid_v3.parquet")
test_df = pd.read_parquet("data/processed/test_v3.parquet")

target_col = "target_excluded_24m"
always_drop = ["npi_clean", "summary_year", target_col]
constant_drop = [
    "tot_benes_missing",
    "tot_srvcs_missing",
    "tot_sbmtd_chrg_missing",
    "tot_mdcr_alowd_amt_missing",
    "tot_mdcr_pymt_amt_missing",
    "tot_mdcr_stdzd_amt_missing",
]
drop_cols = always_drop + [c for c in constant_drop if c in valid_df.columns]
feature_cols = [c for c in valid_df.columns if c not in drop_cols]

model = CatBoostClassifier()
model.load_model("models_v3/final/model.cbm")

score_2022 = model.predict_proba(valid_df[feature_cols])[:, 1]
score_2023 = model.predict_proba(test_df[feature_cols])[:, 1]

score_summary = pd.DataFrame([
    {
        "year": 2022,
        "rows": len(score_2022),
        "mean_score": float(np.mean(score_2022)),
        "std_score": float(np.std(score_2022)),
        "p50_score": float(np.quantile(score_2022, 0.50)),
        "p90_score": float(np.quantile(score_2022, 0.90)),
        "p95_score": float(np.quantile(score_2022, 0.95)),
        "p99_score": float(np.quantile(score_2022, 0.99)),
    },
    {
        "year": 2023,
        "rows": len(score_2023),
        "mean_score": float(np.mean(score_2023)),
        "std_score": float(np.std(score_2023)),
        "p50_score": float(np.quantile(score_2023, 0.50)),
        "p90_score": float(np.quantile(score_2023, 0.90)),
        "p95_score": float(np.quantile(score_2023, 0.95)),
        "p99_score": float(np.quantile(score_2023, 0.99)),
    }
])
score_summary.to_csv(out_dir / "score_drift_summary.csv", index=False)

feature_check_cols = [
    "alowd_to_pymt_ratio",
    "sbmtd_to_alowd_ratio",
    "srvcs_per_bene",
    "alowd_amt_per_bene",
    "tot_benes_specialty_year_pct_rank",
]

rows = []
for col in feature_check_cols:
    rows.append({
        "feature": col,
        "mean_2022": float(valid_df[col].mean()),
        "mean_2023": float(test_df[col].mean()),
        "median_2022": float(valid_df[col].median()),
        "median_2023": float(test_df[col].median()),
        "std_2022": float(valid_df[col].std()),
        "std_2023": float(test_df[col].std()),
    })

feature_summary = pd.DataFrame(rows)
feature_summary.to_csv(out_dir / "feature_drift_summary.csv", index=False)

plt.figure(figsize=(8,5))
plt.hist(score_2022, bins=50, alpha=0.6, label="2022")
plt.hist(score_2023, bins=50, alpha=0.6, label="2023")
plt.legend()
plt.xlabel("Risk score")
plt.ylabel("Count")
plt.title("Score distribution comparison: 2022 vs 2023")
plt.tight_layout()
plt.savefig(out_dir / "score_distribution_2022_vs_2023.png", dpi=200)
plt.close()

note = """
# Monitoring Note

This project includes a simple post-deployment monitoring artifact comparing 2022 and 2023.

Monitored items:
- score distribution shift
- selected feature distribution summaries

Interpretation:
- noticeable shifts may indicate temporal drift
- drift does not automatically mean model failure
- drift should trigger feature review, recalibration, or retraining discussion
- this is a lightweight monitoring deliverable for the class project, not a full production monitoring stack
"""
(out_dir / "MONITORING_NOTE.md").write_text(note.strip(), encoding="utf-8")

print("Saved:")
print(out_dir / "score_drift_summary.csv")
print(out_dir / "feature_drift_summary.csv")
print(out_dir / "score_distribution_2022_vs_2023.png")
print(out_dir / "MONITORING_NOTE.md")
