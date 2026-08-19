# ============================================================
# CELL 9: AER SIMULATOR FACTORY
# ============================================================

def create_simulator(cpu_threads):
    """
    Create an AerSimulator configured with a specified
    maximum number of CPU threads.
    """

    simulator = AerSimulator(
        method="statevector",
        device="CPU",
        max_parallel_threads=cpu_threads,
        max_parallel_experiments=1,
        max_parallel_shots=0
    )

    return simulator
