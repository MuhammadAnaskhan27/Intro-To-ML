import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)


sns.displot(titanic_df["Fare"],kde=True,color='red')
plt.title("Fare Distribution")
plt.show()

sns.boxplot(x='Fare',y='Embarked',data=titanic_df)
plt.title("Boxplot of Fare by Embarked Class")
plt.show()

sns.pairplot(titanic_df[['Age','Fare','Survived']],hue='Survived', palette="husl")
plt.suptitle("Pairplot of Age, Fare, and Survived", y=1.02)
plt.show()