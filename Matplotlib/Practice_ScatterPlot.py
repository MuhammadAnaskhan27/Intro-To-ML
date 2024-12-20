# Create a scatter plot where x is the age of individuals, and y is their height in centimeters.
import matplotlib.pyplot as plt

x = [22,18,12,6,30]
y = [5.9,5.6,5,3.2,6]

plt.scatter(x,y,s=150,color='red')
plt.title("Calculating Height according to Age")
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()