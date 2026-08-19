# ============================================================
# CELL 5: GROVER CIRCUIT GENERATOR
# ============================================================

def create_grover_circuit(n_qubits):
    """
    Create a single-iteration Grover search circuit.

    The marked state is the all-ones state.
    """

    qc = QuantumCircuit(n_qubits, n_qubits)

    # --------------------------------------------------------
    # Step 1: Create equal superposition
    # --------------------------------------------------------
    qc.h(range(n_qubits))

    # --------------------------------------------------------
    # Step 2: Oracle
    # --------------------------------------------------------
    apply_multi_controlled_z(qc)

    # --------------------------------------------------------
    # Step 3: Grover diffusion operator
    # --------------------------------------------------------
    qc.h(range(n_qubits))
    qc.x(range(n_qubits))

    apply_multi_controlled_z(qc)

    qc.x(range(n_qubits))
    qc.h(range(n_qubits))

    # --------------------------------------------------------
    # Two identity operations provide two additional logical
    # execution layers without changing the quantum state.
    # This keeps the experimental circuit structure consistent
    # across all workload sizes.
    # --------------------------------------------------------
    qc.id(0)
    qc.id(0)

    # --------------------------------------------------------
    # Step 4: Measurement
    # --------------------------------------------------------
    qc.measure(range(n_qubits), range(n_qubits))

    return qc
