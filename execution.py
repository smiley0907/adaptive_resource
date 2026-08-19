# ============================================================
# CELL 10: SINGLE TIMED EXECUTION
# ============================================================

def timed_execution(
    simulator,
    circuit,
    shots=SHOTS,
    seed=RANDOM_SEED
):
    """
    Execute one circuit and return execution time in seconds.
    """

    start_time = time.perf_counter()

    job = simulator.run(
        circuit,
        shots=shots,
        seed_simulator=seed
    )

    job.result()

    end_time = time.perf_counter()

    return end_time - start_time
