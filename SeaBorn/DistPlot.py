import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)


sns.displot(titanic_df["Age"].dropna(),color='red',kde=True)
plt.title("Age Distribution")
plt.show()