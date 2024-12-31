import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report

# Load Titanic Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Preprocessing

# Selecting features and target
features = ['Age','Pclass','Fare']
target = 'Survived'

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(),inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(),inplace=True)

# Extract features and target 
x = titanic_df[features]
y = titanic_df[target]

# Splitting datasets into training and testing sets
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Logistic Regression
log_reg = LogisticRegression()
# model training
log_reg.fit(x_train,y_train)
# prediction
y_pred =log_reg.predict(x_test)

# 5. Evaluation
accuracy = accuracy_score(y_test, y_pred)  # DIFFERENT: Metrics used for classification
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report(y_test, y_pred))