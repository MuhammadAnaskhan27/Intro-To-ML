import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Bar plot (Embarked vs. Age)
# We should first aggregate the Age values (mean/median)
sns.barplot(x='Embarked', y='Age', data=titanic_df,)
plt.title("Bar Plot"),
plt.show()

# Count plot (Pclass)
sns.countplot(x='Pclass', data=titanic_df, palette="Set1")
plt.title("Count Plot of Passenger Class")
plt.show()

# Heatmap (Survival by Age and Pclass)
# First, categorize Age into bins for better visualization
age_groups = pd.cut(titanic_df['Age'], bins=[0, 18, 30, 40, 50, 60, 100], labels=['0-18', '19-30', '31-40', '41-50', '51-60', '61+'])

# Create the pivot table for heatmap (mean survival rate)
pivot_table = titanic_df.pivot_table(index=age_groups, columns='Pclass', values='Survived', aggfunc=np.mean)

# Create the heatmap
sns.heatmap(pivot_table, annot=True, cmap='viridis')
plt.title("Survival Rate by Age Group and Passenger Class")
plt.show()
