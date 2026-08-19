# ============================================================
# CELL 15: BEFORE GRAPH
# ============================================================

plt.figure(figsize=(9, 5))

plt.plot(
    baseline_df["Qubits"],
    baseline_df["Median_Time_sec"],
    marker="o"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Median Execution Time (s)")
plt.title("Baseline Static Resource Allocation")
plt.grid(True)
plt.tight_layout()
plt.show()
