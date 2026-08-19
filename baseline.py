# ============================================================
# CELL 12: BEFORE EXPERIMENT
# STATIC RESOURCE ALLOCATION
# ============================================================

baseline_records = []

for n in QUBIT_CONFIGS:

    circuit = circuits[n]
    executable_circuit = execution_circuits[n]

    # --------------------------------------------------------
    # Circuit characteristics
    # --------------------------------------------------------
    gate_count = circuit.size()
    circuit_depth = circuit.depth()

    # --------------------------------------------------------
    # Fixed resource allocation
    # --------------------------------------------------------
    cpu_threads = BASELINE_THREADS

    print(
        f"Running baseline workload: "
        f"{n} qubits | "
        f"{gate_count} gates | "
        f"depth={circuit_depth} | "
        f"threads={cpu_threads}"
    )

    # --------------------------------------------------------
    # Execute workload
    # --------------------------------------------------------
    execution_times = collect_execution_times(
        executable_circuit,
        cpu_threads=cpu_threads,
        warmup_runs=WARMUP_RUNS,
        measurement_runs=MEASUREMENT_RUNS,
        shots=SHOTS,
        seed=RANDOM_SEED + n
    )

    # --------------------------------------------------------
    # Statistical calculations
    # --------------------------------------------------------
    median_time = float(np.median(execution_times))
    mean_time = float(np.mean(execution_times))
    std_time = float(np.std(execution_times, ddof=1))

    min_time = float(np.min(execution_times))
    max_time = float(np.max(execution_times))

    baseline_records.append({
        "Qubits": n,
        "Gate_Count": gate_count,
        "Circuit_Depth": circuit_depth,
        "Shots": SHOTS,
        "CPU_Threads": cpu_threads,
        "Median_Time_sec": median_time,
        "Mean_Time_sec": mean_time,
        "Std_Time_sec": std_time,
        "Min_Time_sec": min_time,
        "Max_Time_sec": max_time
    })

baseline_df = pd.DataFrame(baseline_records)

baseline_df
