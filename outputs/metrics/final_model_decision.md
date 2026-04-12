# Final model decision

## Official final model
- Model: CatBoost v3 final
- Model file: models_v3/final/model.cbm

## Why this model was chosen
- Main CatBoost validation was better than the alternative CatBoost validation
- The final model was retrained on 2018-2022 and tested once on 2023

## Official final test metrics
- AUPRC: 0.0006626745788939973
- ROC-AUC: 0.7676166053703076
- Precision@100: 0.0
- Precision@500: 0.0
- Precision@1000: 0.001
- Precision@5000: 0.0012
- Recall@500: 0.0
- Recall@1000: 0.006666666666666667
- Lift@500: 0.0
- Lift@1000: 8.395553333333334

## Interpretation
- The model learns real signal
- The task remains very difficult because labels are rare and noisy
- The model is better as a risk-ranking tool than as a strict alerting tool for very small top-K review lists
