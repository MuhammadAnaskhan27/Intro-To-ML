import pandas as pd

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Display missing value summary
# print(titanic_df.isnull().sum())

titanic_df["Age_filled_0"] = titanic_df["Age"].fillna(0)
titanic_df["Age_filled_0"] = titanic_df["Age"].fillna(titanic_df["Age"].mean())
titanic_df["Age_filled_0"] = titanic_df["Age"].fillna(titanic_df["Age"].median())
print(titanic_df["Age"].head())