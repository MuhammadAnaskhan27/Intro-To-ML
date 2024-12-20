import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,25,30,35]

plt.scatter(x,y,color='blue',s=50)
plt.xlabel("x-axis")
plt.ylabel('y-axis')
plt.title("Scatter Plot")
plt.show()