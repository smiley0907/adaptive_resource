# ============================================================
# CELL 6: GENERATE GROVER WORKLOADS
# ============================================================

circuits = {}

for n in QUBIT_CONFIGS:
    circuits[n] = create_grover_circuit(n)

print("Generated workloads:")
print()

for n, circuit in circuits.items():
    print(
        f"Qubits={n:2d} | "
        f"Gates={circuit.size():3d} | "
        f"Depth={circuit.depth():2d}"
    )
