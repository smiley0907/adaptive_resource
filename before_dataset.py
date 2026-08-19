# ============================================================
# CELL 14: EXPORT BEFORE DATASET
# ============================================================

baseline_df.to_csv(
    "baseline_results.csv",
    index=False
)

print("Saved: baseline_results.csv")
