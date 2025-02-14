# Import Libraries
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from qiskit import Aer, transpile, assemble
from qiskit.circuit.library import ZFeatureMap, ZZFeatureMap
from qiskit.aqua.algorithms import QSVM
from qiskit.aqua.components.optimizers import COBYLA
from qiskit.aqua import QuantumInstance

# Generate sample data (Features and Labels)
data = np.array([[5, 10], [1, 4], [2, 3], [6, 12], [7, 14], [8, 16]])  # Features (task difficulty, urgency)
labels = np.array([1, 0, 0, 1, 1, 0])  # Labels (high or low priority)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.25)

# Classical ML Model: Random Forest
model = RandomForestClassifier(n_estimators=50)  # Reduced the number of trees for efficiency
model.fit(X_train, y_train)

# Classical Evaluation & Prediction
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Classical ML Accuracy: {accuracy:.2f}")

# Quantum Feature Map Setup for QSVM
feature_map = ZFeatureMap(feature_dimension=2, reps=2)
quantum_instance = QuantumInstance(Aer.get_backend('qasm_simulator'), shots=1024)

# Train Quantum Classifier (QSVM)
qsvm = QSVM(feature_map, quantum_instance=quantum_instance)
qsvm.fit(X_train, y_train)

# Quantum Evaluation & Prediction
quantum_accuracy = accuracy_score(y_test, qsvm.predict(X_test))
print(f"Quantum ML Accuracy: {quantum_accuracy:.2f}")

# PCA for dimensionality reduction (if needed for large quantum feature maps)
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Combining Classical & Quantum Models: Hybrid Approach
# We’ll make predictions with both the classical and quantum models and combine the results.
classical_pred = model.predict(X_test_pca)
quantum_pred = qsvm.predict(X_test_pca)

# Voting System for Final Decision
final_pred = np.round((classical_pred + quantum_pred) / 2).astype(int)
final_accuracy = accuracy_score(y_test, final_pred)

print(f"Hybrid Model Accuracy: {final_accuracy:.2f}")
