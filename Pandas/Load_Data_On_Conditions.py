import pandas as pd

# Load the Titanic dataset from the URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Save the dataset to a local CSV file
titanic_df.to_csv("titanic.csv", index=False)

name_column = titanic_df[['Name','Age']]
age_greater_30 = titanic_df[(titanic_df['Age']>30) & (titanic_df['Sex'] == "male")]
subset = titanic_df.loc[titanic_df['Age'] > 50, ['Name', 'Age']]
print(subset.head())
# print(age_greater_30)
# print(name_column.head())