import numpy as np

# Array and scalar
arr = np.array([1, 2, 3])
result = arr + 10  # Add 10 to each element
print("Result:\n", result)


arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
arr2 = np.array([10, 20, 30])            # Shape (3,)
result = arr1 + arr2
print("Result:\n", result)


arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
arr2 = np.array([[10], [20]])            # Shape (2, 1)
result = arr1 + arr2
print("Result:\n", result)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
arr2 = np.array([10, 20])                # Shape (2,)
result = arr1 + arr2  # ERROR