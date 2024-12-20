import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)
plt.figure(figsize=(8,6))
plt.scatter(
    titanic_df['Age'],
    titanic_df['Fare'],
    c=titanic_df['Survived'],
    cmap='coolwarm',
    alpha=0.6,
    edgecolor='black'
)
plt.title("Scatter Plot: Age vs Fare (Colored by Survival)",fontsize=16)
plt.xlabel("Age",fontsize=14)
plt.ylabel("Fare",fontsize=14)
plt.colorbar(label="Survival (0 = No, 1 = Yes)")
plt.show()
