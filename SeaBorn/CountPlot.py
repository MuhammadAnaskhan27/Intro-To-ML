import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

sns.countplot(x='Survived',data=titanic_df,palette="Set1")
plt.title("Count Plot")
plt.show()