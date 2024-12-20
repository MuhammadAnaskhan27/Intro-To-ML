import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [5,10,20,25,35]

plt.title("Line Plot")
plt.plot(x,y,marker='o',color='blue',linestyle='-')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()