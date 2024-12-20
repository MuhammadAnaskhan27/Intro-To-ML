# Create a 1D NumPy array with the numbers from 10 to 20.
# Reshape it into a 2D array with 2 rows and 5 columns.
# Slice and print the first 2 rows and the last 3 columns of the reshaped array.
# Create a 3x3 array of ones and a 3x3 array of zeros, then subtract the zero array from the ones array.
# Create a 5x5 array with values from 0 to 24 and slice the middle 3x3 part of the array.

import numpy as np


arr_1d = np.array([11,12,13,14,15,16,17,18,19,20])
reshaped_arr = arr_1d.reshape((2,5))
print(reshaped_arr)
sliced_arr = reshaped_arr[:2,:3]
print(sliced_arr)
arr_ones = np.ones((3,3))
arr_zeros = np.zeros((3,3))
subtracted_arr = arr_ones - arr_zeros
print(subtracted_arr)
arr_5d = np.arange(25).reshape(5,5)
print(arr_5d)
middle_3x3 = arr_5d[1:4, 1:4]  # Selecting rows 1 to 3 (inclusive) and columns 1 to 3 (inclusive)
print(middle_3x3)