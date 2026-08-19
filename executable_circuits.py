# ============================================================
# CELL 8: PREPARE CIRCUITS FOR EXECUTION
# ============================================================

# The logical circuit is used for:
#   - qubit count
#   - gate count
#   - circuit depth
#
# A transpiled copy is used for simulator execution.
# Transpilation is performed outside the timing loop so that
# compilation time is not included in execution-time measurements.

execution_circuits = {}

for n, circuit in circuits.items():

    simulator = AerSimulator()

    execution_circuits[n] = transpile(
        circuit,
        simulator,
        optimization_level=0,
        seed_transpiler=RANDOM_SEED
    )

print("Execution circuits prepared.")
