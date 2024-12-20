import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)


sns.boxplot(x='Pclass',y='Age',data=titanic_df)
plt.title("Boxplot of Age by Passenger Class")
plt.show()