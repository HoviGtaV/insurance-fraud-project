from pathlib import Path
import pandas as pd

out_dir = Path("submission/docs")
out_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_parquet("data/processed/test_v3.parquet")

def describe_col(c):
    if c == "npi_clean":
        return ("identifier", "Clean provider NPI used as the provider identifier")
    if c == "summary_year":
        return ("time", "Provider summary year")
    if c == "rndrng_prvdr_type":
        return ("categorical_feature", "Provider specialty / rendering provider type")
    if c == "target_excluded_24m":
        return ("target", "Proxy label: 1 if exclusion occurs within 24 months after year end, else 0")
    if c in ["tot_benes", "tot_srvcs", "tot_sbmtd_chrg", "tot_mdcr_alowd_amt", "tot_mdcr_pymt_amt", "tot_mdcr_stdzd_amt"]:
        return ("raw_feature", f"Raw provider-year total for {c}")
    if c.endswith("_missing"):
        return ("missingness_flag", f"Missingness indicator for {c.replace('_missing','')}")
    if c.endswith("_per_bene"):
        return ("ratio_feature", f"Provider-year normalized per beneficiary: {c}")
    if c.endswith("_per_srvc"):
        return ("ratio_feature", f"Provider-year normalized per service: {c}")
    if c in ["sbmtd_to_alowd_ratio", "alowd_to_pymt_ratio", "stdzd_to_pymt_ratio", "sbmtd_to_pymt_ratio"]:
        return ("structural_ratio_feature", f"Cross-financial ratio feature: {c}")
    if c.startswith("log1p_"):
        return ("log_feature", f"Log(1+x) transform of {c.replace('log1p_','')}")
    if c.endswith("_specialty_year_median"):
        base = c.replace("_specialty_year_median","")
        return ("peer_reference_feature", f"Median value of {base} within the same summary year and provider specialty")
    if c.endswith("_minus_specialty_year_median"):
        base = c.replace("_minus_specialty_year_median","")
        return ("peer_deviation_feature", f"Difference between provider value and specialty-year median for {base}")
    if c.endswith("_specialty_year_pct_rank"):
        base = c.replace("_specialty_year_pct_rank","")
        return ("peer_percentile_feature", f"Percentile rank of {base} within the same summary year and provider specialty")
    if c.startswith("flag_top1pct_"):
        return ("rarity_flag", f"Top 1 percent flag within specialty-year group: {c}")
    if c.startswith("flag_top5pct_"):
        return ("rarity_flag", f"Top 5 percent flag within specialty-year group: {c}")
    return ("other", f"Feature column: {c}")

rows = []
for c in df.columns:
    role, desc = describe_col(c)
    rows.append({
        "column_name": c,
        "dtype": str(df[c].dtype),
        "role": role,
        "description": desc
    })

dd = pd.DataFrame(rows)
dd.to_csv(out_dir / "data_dictionary_v3_full.csv", index=False)

md_lines = ["# Full Data Dictionary (v3)", ""]
for _, r in dd.iterrows():
    md_lines.append(f"## {r['column_name']}")
    md_lines.append(f"- dtype: {r['dtype']}")
    md_lines.append(f"- role: {r['role']}")
    md_lines.append(f"- description: {r['description']}")
    md_lines.append("")

(out_dir / "DATA_DICTIONARY_V3_FULL.md").write_text("\n".join(md_lines), encoding="utf-8")

print("Saved:")
print(out_dir / "data_dictionary_v3_full.csv")
print(out_dir / "DATA_DICTIONARY_V3_FULL.md")
