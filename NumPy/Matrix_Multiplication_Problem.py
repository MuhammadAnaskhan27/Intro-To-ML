import numpy as np

C = np.array([[2,4],[6,8]])
D = np.array([[1,3],[5,7]])
E = np.array([[9,6,3],[8,5,2],[7,4,1]])
F = np.array([[3,1],[2,4]])
matrix_multiplication = np.dot(C,D)
matrix_transposition = E.T
matrix_inverse = np.linalg.inv(F)
matrix_identity = np.dot(F,matrix_inverse)
print(matrix_multiplication)
print(matrix_transposition)
print(matrix_inverse)
print(matrix_identity)
