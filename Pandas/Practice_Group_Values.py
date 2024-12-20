# Group passengers by Embarked and calculate the average Fare for each embarkation point.
# Group by Pclass and calculate the total number of passengers in each class.
# Group by Pclass and Survived, and calculate the median Age for each group.

import pandas as pd

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

passengers = titanic_df.groupby('Embarked')['Fare'].mean()
number_of_passengers = titanic_df.groupby(['Pclass','Survived'])['Age'].median()
print(number_of_passengers)
print(passengers)

