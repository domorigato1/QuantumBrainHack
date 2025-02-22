from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit import Aer
from qiskit.providers.aer import AerSimulator

backend = Aer.get_backend('qasm_simulator')  # Define the backend
simulator = AerSimulator.from_backend(backend)  # Now pass it into AerSimulator


# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate on the first qubit (superposition)
qc.h(0)

# Apply a CNOT gate (entanglement)
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Run on the Aer simulator
simulator = Aer.get_backend('aer_simulator')
qc = transpile(qc, simulator)
qobj = assemble(qc)
result = simulator.run(qobj).result()
counts = result.get_counts()

# Show results
print(counts)
plot_histogram(counts)
plt.show()
