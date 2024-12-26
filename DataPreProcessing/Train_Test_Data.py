from sklearn.model_selection import train_test_split
import pandas as pd


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

X = titanic_df[['Age','Fare','Pclass']]
Y = titanic_df[['Survived']]

X['Age'].fillna(X['Age'].median())

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print('Training set size:',X_train.shape)
print('Testing set size:',X_test.shape)

