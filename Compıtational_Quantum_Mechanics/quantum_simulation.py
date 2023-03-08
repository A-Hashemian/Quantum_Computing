import numpy as np

# create a Bell state (a quantum connection between two qubits)
qubit1 = np.array([[1], [0]])
qubit2 = np.array([[1], [0]])
bell_state = np.kron(qubit1, qubit2) * np.sqrt(2)
