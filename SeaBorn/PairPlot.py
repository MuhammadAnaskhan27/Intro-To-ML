import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)


sns.pairplot(titanic_df[['Age', 'Fare', 'Pclass']], hue='Pclass', palette="husl")
plt.suptitle("Pairplot of Age, Fare, and Pclass", y=1.02)
plt.show()
