from pathlib import Path
import pandas as pd

required = [
    "README.md",
    "TEAM_CONTRIBUTIONS.md",
    "Dockerfile",
    "requirements.txt",
    "score_batch_v3.py",
    "models_v3/final/model.cbm",
    "models_v3/final/metrics_test.json",
    "outputs/shap/shap_summary_bar.png",
    "outputs/shap/shap_beeswarm.png",
    "outputs/shap/global_shap_importance.csv",
    "outputs/shap/local_explanations_top5.csv",
    "submission/docs/LABEL_POLICY_APPENDIX.md",
    "submission/docs/data_dictionary_v3_full.csv",
    "submission/docs/DATA_DICTIONARY_V3_FULL.md",
    "submission/docs/PIPELINE_TRACE.md",
    "submission/monitoring/score_drift_summary.csv",
    "submission/monitoring/feature_drift_summary.csv",
    "submission/monitoring/score_distribution_2022_vs_2023.png",
    "submission/monitoring/MONITORING_NOTE.md",
    "submission/report/report_one_page_final.md",
    "submission/slides/presentation_final_content.md",
    "submission/video/video_demo_script_final.md",
    "submission/qa/check_final_feature_tables_v3.csv",
    "submission/qa/check_final_labels_v3.csv",
    "submission/qa/check_oig_date_consistency_v3.csv"
]

rows = []
for p in required:
    exists = Path(p).exists()
    rows.append({"file": p, "exists": exists})

df = pd.DataFrame(rows)
Path("submission/qa").mkdir(parents=True, exist_ok=True)
df.to_csv("submission/qa/final_submission_checklist.csv", index=False)

print(df.to_string(index=False))
print("\nSaved: submission/qa/final_submission_checklist.csv")
