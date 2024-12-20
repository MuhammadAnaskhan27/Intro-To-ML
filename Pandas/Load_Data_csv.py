import pandas as pd

# Load the Titanic dataset from the URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Save the dataset to a local CSV file
titanic_df.to_csv("titanic.csv", index=False)

# display 5 rows
print(titanic_df.head())  
# display column names
print(titanic_df.columns)
# display data types
print(titanic_df.dtypes)
# display shapes
print(titanic_df.shape)
