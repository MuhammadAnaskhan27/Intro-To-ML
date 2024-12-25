from sklearn.preprocessing import MinMaxScaler
import pandas as pd


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

titanic_df["Age"].fillna(titanic_df["Age"].median())
titanic_df["Fare"].fillna(titanic_df["Fare"].median())
columns_to_normalize = ['Age','Fare']
normalizer = MinMaxScaler()

titanic_df[columns_to_normalize] = normalizer.fit_transform(titanic_df[columns_to_normalize])

print(titanic_df[columns_to_normalize].head(3))