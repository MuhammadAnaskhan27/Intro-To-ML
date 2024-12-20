import pandas as pd

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)


# Interpolate missing 'Age' values linearly
titanic_df['Age_interpolated'] = titanic_df['Age'].interpolate(method='linear')

# Interpolate missing 'Age' using polynomial method
titanic_df['Age_polynomial'] = titanic_df['Age'].interpolate(method='polynomial', order=2)
