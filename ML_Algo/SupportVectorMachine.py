from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from sklearn.model_selection import train_test_split

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


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 2. Model Initialization (Specific to SVM)
svm_model = SVC(kernel='rbf', C=1)  # DIFFERENT: Kernel type and regularization parameter

# 3. Model Training
svm_model.fit(X_train, y_train)

# 4. Predictions
y_pred = svm_model.predict(X_test)

# 5. Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
