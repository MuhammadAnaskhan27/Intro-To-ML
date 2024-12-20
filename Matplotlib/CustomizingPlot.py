import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]
plt.figure(figsize=(8,6))
plt.plot(x,y,color='green',label='squared numbers',marker='o',linestyle='--')
plt.xlabel('numbers',fontsize='12')
plt.ylabel('squares',fontsize=12)
plt.title("Customized Line Plot: Numbers and Their Squares", fontsize=16, color='darkblue')  
plt.grid(linestyle='--',color='grey',linewidth=0.5)
plt.legend(loc='upper left')
plt.show()