import pandas as pd

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Group data by 'Pclass' and calculate the mean of 'Age'
mean_age_by_class = titanic_df.groupby('Pclass')['Age'].mean()
# print(mean_age_by_class)
surival_rate_by_class_gender = titanic_df.groupby(['Pclass','Sex'])['Survived'].mean()
# print(surival_rate_by_class_gender)


# Group by 'Pclass' and perform multiple aggregate calculations on 'Fare'
fare_stats = titanic_df.groupby('Pclass')['Fare'].agg(['count', 'mean', 'median'])
print(fare_stats)



