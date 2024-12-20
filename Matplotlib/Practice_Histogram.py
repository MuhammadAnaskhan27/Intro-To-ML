import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(500)

plt.hist(data,bins=30,color='red',edgecolor='black')
plt.title("Histogram of 500 random numbers")
plt.xlabel("x-axis")
plt.ylabel('y-axis')
plt.show()