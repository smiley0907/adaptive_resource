# ============================================================
# CELL 3: EXPERIMENT CONFIGURATION
# ============================================================

# Quantum workload configurations
QUBIT_CONFIGS = [3, 5, 7, 9, 11]

# Number of measurement shots
SHOTS = 1024

# Baseline CPU allocation
BASELINE_THREADS = 4

# Adaptive candidate CPU configurations
ADAPTIVE_CANDIDATES = [2, 4]

# Warm-up executions
WARMUP_RUNS = 2

# Final measurement repetitions
MEASUREMENT_RUNS = 10

# Adaptive resource selection runs
SELECTION_RUNS = 3

# Reproducibility
RANDOM_SEED = 42

print("Qubit configurations :", QUBIT_CONFIGS)
print("Shots                :", SHOTS)
print("Baseline threads     :", BASELINE_THREADS)
print("Adaptive candidates  :", ADAPTIVE_CANDIDATES)
print("Warm-up runs         :", WARMUP_RUNS)
print("Measurement runs     :", MEASUREMENT_RUNS)
print("Selection runs       :", SELECTION_RUNS)
