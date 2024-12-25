import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)
titanic_df["Age"] = titanic_df["Age"].fillna(titanic_df["Age"].median())
titanic_df['Cabin'] = titanic_df['Cabin'].fillna('Unknown')
titanic_df = titanic_df.dropna(subset=['Embarked'])
titanic_df["Fare"] = titanic_df["Fare"].interpolate(method='linear')
print(titanic_df.isnull().sum())