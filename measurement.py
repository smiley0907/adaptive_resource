# ============================================================
# CELL 11: REPEATED EXECUTION
# ============================================================

def collect_execution_times(
    circuit,
    cpu_threads,
    warmup_runs=WARMUP_RUNS,
    measurement_runs=MEASUREMENT_RUNS,
    shots=SHOTS,
    seed=RANDOM_SEED
):
    """
    Perform warm-up executions followed by repeated
    measurement executions.
    """

    simulator = create_simulator(cpu_threads)

    # --------------------------------------------------------
    # Warm-up phase
    # --------------------------------------------------------
    for i in range(warmup_runs):

        timed_execution(
            simulator,
            circuit,
            shots=shots,
            seed=seed + i
        )

    # --------------------------------------------------------
    # Measurement phase
    # --------------------------------------------------------
    execution_times = []

    for i in range(measurement_runs):

        elapsed = timed_execution(
            simulator,
            circuit,
            shots=shots,
            seed=seed + warmup_runs + i
        )

        execution_times.append(elapsed)

    return execution_times
