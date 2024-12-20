# Select and display the Name and Survived columns.
# Filter passengers:
# Who are in Pclass 3.
# Whose age is between 20 and 40.
# Who embarked at 'S' (Southampton).
# Combine filtering:
# Passengers younger than 18 who survived.
# Filter rows where passengers survived and are female.

import pandas as pd

# Load the Titanic dataset from the URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Save the dataset to a local CSV file
titanic_df.to_csv("titanic.csv", index=False)

name_survivors = titanic_df[ ['Name','Survived']]
p_class = titanic_df[titanic_df['Pclass']==3]
age = titanic_df[(titanic_df['Age'] > 20) & (titanic_df['Age']<40) ]
embarked = titanic_df[titanic_df['Embarked'] == "S" ]
young_survivors = titanic_df.loc[(titanic_df['Age']<18), ['Age','Survived']]
female_survivors = titanic_df[(titanic_df['Survived']=="female")]
print("Passengers younger than 18 who survived:" ,young_survivors.head())
print("Who embarked at 'S' (Southampton):" ,embarked.head())
print("Whose age is between 20 and 40:" ,age.head())
print("Select and display the Name and Survived columns:",name_survivors.head())
print( "Who are in Pclass 3:" ,p_class.head())

