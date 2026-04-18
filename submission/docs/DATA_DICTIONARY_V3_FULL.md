# Full Data Dictionary (v3)

## npi_clean
- dtype: str
- role: identifier
- description: Clean provider NPI used as the provider identifier

## summary_year
- dtype: int64
- role: time
- description: Provider summary year

## rndrng_prvdr_type
- dtype: str
- role: categorical_feature
- description: Provider specialty / rendering provider type

## target_excluded_24m
- dtype: int64
- role: target
- description: Proxy label: 1 if exclusion occurs within 24 months after year end, else 0

## tot_benes
- dtype: int64
- role: raw_feature
- description: Raw provider-year total for tot_benes

## tot_srvcs
- dtype: float64
- role: raw_feature
- description: Raw provider-year total for tot_srvcs

## tot_sbmtd_chrg
- dtype: float64
- role: raw_feature
- description: Raw provider-year total for tot_sbmtd_chrg

## tot_mdcr_alowd_amt
- dtype: float64
- role: raw_feature
- description: Raw provider-year total for tot_mdcr_alowd_amt

## tot_mdcr_pymt_amt
- dtype: float64
- role: raw_feature
- description: Raw provider-year total for tot_mdcr_pymt_amt

## tot_mdcr_stdzd_amt
- dtype: float64
- role: raw_feature
- description: Raw provider-year total for tot_mdcr_stdzd_amt

## tot_benes_missing
- dtype: int64
- role: missingness_flag
- description: Missingness indicator for tot_benes

## tot_srvcs_missing
- dtype: int64
- role: missingness_flag
- description: Missingness indicator for tot_srvcs

## tot_sbmtd_chrg_missing
- dtype: int64
- role: missingness_flag
- description: Missingness indicator for tot_sbmtd_chrg

## tot_mdcr_alowd_amt_missing
- dtype: int64
- role: missingness_flag
- description: Missingness indicator for tot_mdcr_alowd_amt

## tot_mdcr_pymt_amt_missing
- dtype: int64
- role: missingness_flag
- description: Missingness indicator for tot_mdcr_pymt_amt

## tot_mdcr_stdzd_amt_missing
- dtype: int64
- role: missingness_flag
- description: Missingness indicator for tot_mdcr_stdzd_amt

## srvcs_per_bene
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per beneficiary: srvcs_per_bene

## sbmtd_chrg_per_bene
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per beneficiary: sbmtd_chrg_per_bene

## alowd_amt_per_bene
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per beneficiary: alowd_amt_per_bene

## pymt_amt_per_bene
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per beneficiary: pymt_amt_per_bene

## sbmtd_chrg_per_srvc
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per service: sbmtd_chrg_per_srvc

## alowd_amt_per_srvc
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per service: alowd_amt_per_srvc

## pymt_amt_per_srvc
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per service: pymt_amt_per_srvc

## sbmtd_to_alowd_ratio
- dtype: float64
- role: structural_ratio_feature
- description: Cross-financial ratio feature: sbmtd_to_alowd_ratio

## alowd_to_pymt_ratio
- dtype: float64
- role: structural_ratio_feature
- description: Cross-financial ratio feature: alowd_to_pymt_ratio

## stdzd_to_pymt_ratio
- dtype: float64
- role: structural_ratio_feature
- description: Cross-financial ratio feature: stdzd_to_pymt_ratio

## sbmtd_to_pymt_ratio
- dtype: float64
- role: structural_ratio_feature
- description: Cross-financial ratio feature: sbmtd_to_pymt_ratio

## log1p_tot_benes
- dtype: float64
- role: log_feature
- description: Log(1+x) transform of tot_benes

## log1p_tot_srvcs
- dtype: float64
- role: log_feature
- description: Log(1+x) transform of tot_srvcs

## log1p_tot_sbmtd_chrg
- dtype: float64
- role: log_feature
- description: Log(1+x) transform of tot_sbmtd_chrg

## log1p_tot_mdcr_alowd_amt
- dtype: float64
- role: log_feature
- description: Log(1+x) transform of tot_mdcr_alowd_amt

## log1p_tot_mdcr_pymt_amt
- dtype: float64
- role: log_feature
- description: Log(1+x) transform of tot_mdcr_pymt_amt

## log1p_tot_mdcr_stdzd_amt
- dtype: float64
- role: log_feature
- description: Log(1+x) transform of tot_mdcr_stdzd_amt

## log1p_srvcs_per_bene
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per beneficiary: log1p_srvcs_per_bene

## log1p_sbmtd_chrg_per_bene
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per beneficiary: log1p_sbmtd_chrg_per_bene

## log1p_alowd_amt_per_bene
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per beneficiary: log1p_alowd_amt_per_bene

## log1p_pymt_amt_per_bene
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per beneficiary: log1p_pymt_amt_per_bene

## log1p_sbmtd_chrg_per_srvc
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per service: log1p_sbmtd_chrg_per_srvc

## log1p_alowd_amt_per_srvc
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per service: log1p_alowd_amt_per_srvc

## log1p_pymt_amt_per_srvc
- dtype: float64
- role: ratio_feature
- description: Provider-year normalized per service: log1p_pymt_amt_per_srvc

## tot_benes_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_benes within the same summary year and provider specialty

## tot_benes_minus_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_benes_minus within the same summary year and provider specialty

## tot_benes_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of tot_benes within the same summary year and provider specialty

## tot_srvcs_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_srvcs within the same summary year and provider specialty

## tot_srvcs_minus_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_srvcs_minus within the same summary year and provider specialty

## tot_srvcs_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of tot_srvcs within the same summary year and provider specialty

## tot_sbmtd_chrg_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_sbmtd_chrg within the same summary year and provider specialty

## tot_sbmtd_chrg_minus_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_sbmtd_chrg_minus within the same summary year and provider specialty

## tot_sbmtd_chrg_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of tot_sbmtd_chrg within the same summary year and provider specialty

## tot_mdcr_alowd_amt_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_mdcr_alowd_amt within the same summary year and provider specialty

## tot_mdcr_alowd_amt_minus_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_mdcr_alowd_amt_minus within the same summary year and provider specialty

## tot_mdcr_alowd_amt_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of tot_mdcr_alowd_amt within the same summary year and provider specialty

## tot_mdcr_pymt_amt_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_mdcr_pymt_amt within the same summary year and provider specialty

## tot_mdcr_pymt_amt_minus_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_mdcr_pymt_amt_minus within the same summary year and provider specialty

## tot_mdcr_pymt_amt_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of tot_mdcr_pymt_amt within the same summary year and provider specialty

## tot_mdcr_stdzd_amt_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_mdcr_stdzd_amt within the same summary year and provider specialty

## tot_mdcr_stdzd_amt_minus_specialty_year_median
- dtype: float64
- role: peer_reference_feature
- description: Median value of tot_mdcr_stdzd_amt_minus within the same summary year and provider specialty

## tot_mdcr_stdzd_amt_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of tot_mdcr_stdzd_amt within the same summary year and provider specialty

## srvcs_per_bene_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of srvcs_per_bene within the same summary year and provider specialty

## sbmtd_chrg_per_bene_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of sbmtd_chrg_per_bene within the same summary year and provider specialty

## alowd_amt_per_bene_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of alowd_amt_per_bene within the same summary year and provider specialty

## pymt_amt_per_bene_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of pymt_amt_per_bene within the same summary year and provider specialty

## sbmtd_to_alowd_ratio_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of sbmtd_to_alowd_ratio within the same summary year and provider specialty

## alowd_to_pymt_ratio_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of alowd_to_pymt_ratio within the same summary year and provider specialty

## sbmtd_to_pymt_ratio_specialty_year_pct_rank
- dtype: float64
- role: peer_percentile_feature
- description: Percentile rank of sbmtd_to_pymt_ratio within the same summary year and provider specialty

## flag_top1pct_tot_srvcs_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 1 percent flag within specialty-year group: flag_top1pct_tot_srvcs_within_specialty_year

## flag_top5pct_tot_srvcs_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 5 percent flag within specialty-year group: flag_top5pct_tot_srvcs_within_specialty_year

## flag_top1pct_tot_mdcr_pymt_amt_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 1 percent flag within specialty-year group: flag_top1pct_tot_mdcr_pymt_amt_within_specialty_year

## flag_top5pct_tot_mdcr_pymt_amt_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 5 percent flag within specialty-year group: flag_top5pct_tot_mdcr_pymt_amt_within_specialty_year

## flag_top1pct_tot_mdcr_alowd_amt_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 1 percent flag within specialty-year group: flag_top1pct_tot_mdcr_alowd_amt_within_specialty_year

## flag_top5pct_tot_mdcr_alowd_amt_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 5 percent flag within specialty-year group: flag_top5pct_tot_mdcr_alowd_amt_within_specialty_year

## flag_top1pct_srvcs_per_bene_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 1 percent flag within specialty-year group: flag_top1pct_srvcs_per_bene_within_specialty_year

## flag_top5pct_srvcs_per_bene_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 5 percent flag within specialty-year group: flag_top5pct_srvcs_per_bene_within_specialty_year

## flag_top1pct_sbmtd_to_pymt_ratio_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 1 percent flag within specialty-year group: flag_top1pct_sbmtd_to_pymt_ratio_within_specialty_year

## flag_top5pct_sbmtd_to_pymt_ratio_within_specialty_year
- dtype: int64
- role: rarity_flag
- description: Top 5 percent flag within specialty-year group: flag_top5pct_sbmtd_to_pymt_ratio_within_specialty_year

