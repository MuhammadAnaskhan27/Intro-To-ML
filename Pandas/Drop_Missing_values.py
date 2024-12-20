import pandas as pd

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Drop rows with any missing values
rows_dropped_df = titanic_df.dropna()
print("Shape after dropping rows:", rows_dropped_df.shape)

# Drop columns with any missing values
columns_dropped_df = titanic_df.dropna(axis=1)
print("Shape after dropping columns:", columns_dropped_df.shape)

# Drop rows where 'Cabin' is missing
rows_dropped_cabin = titanic_df[titanic_df['Cabin'].notnull()]
print("Shape after dropping rows with missing 'Cabin':", rows_dropped_cabin.shape)
