import numpy as np

# create a Bell state (a quantum connection between two qubits)
qubit1 = np.array([[1], [0]])
qubit2 = np.array([[1], [0]])
bell_state = np.kron(qubit1, qubit2) * np.sqrt(2)


# create the Hadamard matrix
hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

# apply the Hadamard matrix to the first qubit
qubit1 = np.dot(hadamard, qubit1)

# break the quantum connection between the first and second qubits in the Bell state
cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
bell_state = np.dot(cnot, bell_state)
