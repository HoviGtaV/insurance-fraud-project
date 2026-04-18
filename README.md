# Insurance Fraud Project — Provider-Level Medicare Risk Scoring

## Project Summary
This project builds a provider-level Medicare fraud-risk scoring system using public Medicare provider summary data and OIG exclusion-based proxy labels.

Important framing:
- This is a **risk scoring** system
- This is **not** a legal fraud detector
- Exclusion labels are **proxy labels**, not perfect ground truth
- The output should be used to rank providers for review, not to prove wrongdoing

## Business Question
Given this provider summary profile, how risky does the pattern look compared with providers later excluded from federal healthcare programs?

## Data Sources
- CMS Medicare provider summary data, 2017-2023
- OIG LEIE exclusion data

## Unit of Analysis
- One row = one provider-year
- Provider identifier = `npi_clean`
- Time field = `summary_year`

## Label Definition
Target:
- `target_excluded_24m`

Meaning:
- `1` if provider exclusion occurs within 24 months after the provider-year end
- `0` otherwise, after censoring and exclusion rules

Rows with same-year or earlier exclusions are removed from modeling to avoid leakage.

See:
- `submission/docs/LABEL_POLICY_APPENDIX.md`

## Pipeline Trace
See:
- `submission/docs/PIPELINE_TRACE.md`

## Feature Engineering
The final v3 pipeline includes:
- raw utilization and payment totals
- per-beneficiary and per-service ratios
- structural payment ratios
- log-transformed features
- specialty-year medians
- specialty-year percentile ranks
- deviations from specialty-year medians
- rarity flags for top-1% and top-5% extreme values

## Split Design
Final modeling split:
- Train: 2018-2021
- Validation: 2022
- Final train for official model: 2018-2022
- Final untouched holdout test: 2023

## Models
Baseline:
- Logistic Regression

Main model:
- CatBoost

Official final model:
- `models_v3/final/model.cbm`

## Final Official Test Metrics
2023 holdout test:
- AUPRC: 0.0006626745788939973
- ROC-AUC: 0.7676166053703076
- Precision@100: 0.0
- Precision@500: 0.0
- Precision@1000: 0.001
- Precision@5000: 0.0012
- Recall@1000: 0.006666666666666667
- Lift@1000: 8.395553333333334

## Interpretation of Results
The final model captures real ranking signal above random selection in an extremely imbalanced proxy-label setting. However, top-K precision remains limited, especially for very small review queues. Therefore, the model should be interpreted as a **broad risk-ranking tool**, not a high-precision fraud adjudication system.

## Explainability
The project includes SHAP-based explainability:
- global SHAP feature importance
- SHAP summary bar plot
- SHAP beeswarm plot
- local explanations for top scored provider-year examples

Key outputs:
- `outputs/shap/global_shap_importance.csv`
- `outputs/shap/shap_summary_bar.png`
- `outputs/shap/shap_beeswarm.png`
- `outputs/shap/local_explanations_top5.csv`

## Monitoring
The project includes simple post-deployment monitoring artifacts:
- `submission/monitoring/score_drift_summary.csv`
- `submission/monitoring/feature_drift_summary.csv`
- `submission/monitoring/score_distribution_2022_vs_2023.png`
- `submission/monitoring/MONITORING_NOTE.md`

## Data Dictionary
See:
- `submission/docs/data_dictionary_v3_full.csv`
- `submission/docs/DATA_DICTIONARY_V3_FULL.md`

## Batch Scoring
The deployed scorer is:
- `score_batch_v3.py`

Important:
- it expects a **feature-ready provider-year table**
- it does **not** accept raw CMS/OIG tables directly
- it is strongest as a **batch scoring** tool, not raw real-time single-record scoring

Example:
python score_batch_v3.py --input examples/sample_input_v3.csv --model models_v3/final/model.cbm --output examples/sample_output_v3.csv

## Docker
Build:
docker build -t insurance-fraud-risk:latest .

Run:
docker run --rm -v "${PWD}\examples:/app/examples" insurance-fraud-risk:latest python score_batch_v3.py --input /app/examples/sample_input_v3.csv --model /app/models_v3/final/model.cbm --output /app/examples/sample_output_docker_v3.csv

## Repository Structure
- root = final active v3 scripts
- `src/cleaning` = cleaning and schema audit evidence
- `src/labels` = exclusion history, join, and label creation evidence
- `src/qa` = QA evidence
- `src/legacy` = older non-final development history
- `models_v3/final` = official final model artifacts
- `outputs` = metrics and SHAP outputs
- `examples` = batch-scoring demo files
- `submission` = final submission materials

## Limitations
- Exclusion is a proxy label, not legal fraud ground truth
- Extreme class imbalance makes small top-K precision difficult
- Public summary data is weaker than claim-level or investigative data
- Specialty-year normalization supports batch scoring better than single-record online scoring

## Team Contributions
See:
- `TEAM_CONTRIBUTIONS.md`

