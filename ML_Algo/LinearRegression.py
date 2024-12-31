import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
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

# Linear Regression
lin_reg = LinearRegression()

# Model Training
lin_reg.fit(x_train,y_train)

# Predictions
y_pred = lin_reg.predict(x_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)  # DIFFERENT: Metrics used for regression
print(f"Mean Squared Error: {mse}")

