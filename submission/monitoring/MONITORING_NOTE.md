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