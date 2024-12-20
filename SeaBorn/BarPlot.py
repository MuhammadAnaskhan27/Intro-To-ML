import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

sns.barplot(x='Pclass',y='Fare',data=titanic_df,palette='coolwarm')
plt.title("Barplot")
plt.show()