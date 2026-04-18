# FINAL PIPELINE MAP

## Official final active pipeline
1. src/cleaning/build_cms_all_years_clean.py
2. src/labels/build_exclusion_history.py
3. src/labels/build_provider_year_joined.py
4. src/labels/build_provider_year_labeled.py
5. build_provider_year_features_v3.py
6. make_v3_splits.py
7. train_logreg_v3.py
8. train_catboost_v3.py
9. retrain_and_test_final_catboost_v3.py
10. explain_shap_v3.py
11. analyze_topk_v3.py
12. score_batch_v3.py

## Support / audit files
- audit_provider_year_features_v3.py
- src/cleaning/Column_Cleaning.py
- src/cleaning/schema_audit.py
- src/qa/check_final_feature_tables_v3.py
- src/qa/check_final_labels_v3.py
- src/qa/check_oig_date_consistency_v3.py
- src/qa/npi_join_test.py
- submission/tools/*

## Historical but kept on purpose
- src/legacy/*

## Not part of the final active submission path
- anything under _archive_local_not_for_git
- local review bundles
- local freeze snapshots
- local review-stage folders

