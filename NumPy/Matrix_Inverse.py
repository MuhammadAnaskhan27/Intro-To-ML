# Matrix inversion

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = A @ B  # or np.dot(A, B)
print("Matrix Multiplication:\n", result)
inverse_A = np.linalg.inv(A)
print("\nInverse of Matrix A:\n", inverse_A)

# Verify: A @ A^(-1) = Identity matrix
identity_matrix = A @ inverse_A
print("\nVerification (Identity Matrix):\n", identity_matrix)
