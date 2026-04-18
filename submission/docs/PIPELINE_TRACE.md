# PIPELINE TRACE

## Raw CMS to cleaned CMS
Script:
- src/cleaning/build_cms_all_years_clean.py

Inputs:
- data/raw/cms/mup_provider_2017.csv
- data/raw/cms/mup_provider_2018.csv
- data/raw/cms/mup_provider_2019.csv
- data/raw/cms/mup_provider_2020.csv
- data/raw/cms/mup_provider_2021.csv
- data/raw/cms/mup_provider_2022.csv
- data/raw/cms/mup_provider_2023.csv

Outputs:
- data/interim/cms_all_years_clean.parquet
- data/interim/cms_2023_clean.parquet
- data/interim/cms_all_years_clean_build_log.csv

## OIG exclusion history
Script:
- src/labels/build_exclusion_history.py

## Provider-year join
Script:
- src/labels/build_provider_year_joined.py

## Label creation
Script:
- src/labels/build_provider_year_labeled.py

## Final v3 feature generation
Script:
- build_provider_year_features_v3.py

## Final v3 split
Script:
- make_v3_splits.py

## Baseline
Script:
- train_logreg_v3.py

## Main model
Script:
- train_catboost_v3.py

## Final retrain and holdout test
Script:
- retrain_and_test_final_catboost_v3.py

## Explainability
Script:
- explain_shap_v3.py

## Ranking analysis
Script:
- analyze_topk_v3.py

## Deployment
Script:
- score_batch_v3.py

