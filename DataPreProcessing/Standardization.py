from sklearn.preprocessing import StandardScaler
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

titanic_df["Age"].fillna(titanic_df["Age"].median())
titanic_df["Fare"].fillna(titanic_df["Fare"].median())

columns_to_scale = ['Age','Fare'] 

scaler = StandardScaler()

titanic_df[columns_to_scale] = scaler.fit_transform(titanic_df[columns_to_scale])
print(titanic_df[columns_to_scale].head())