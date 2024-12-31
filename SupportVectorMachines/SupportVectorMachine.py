import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load the Titanic Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Pre-Processing

# Selecting Features and Target
features = ['Pclass', 'Age', 'Fare']
target = 'Survived'

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(), inplace=True)

# Extract Features and Target
X = titanic_df[features]
y = titanic_df[target]

# Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize Features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Building the SVM Classifier
svm_model = SVC(kernel='linear')  # Linear kernel SVM
svm_model.fit(X_train_scaled, y_train)

# Predicting on Test Data
y_pred = svm_model.predict(X_test_scaled)

# Evaluate Model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Classification Report
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)

# Visualizing the decision boundary (only for 2 features)
# For simplicity, we'll visualize the decision boundary using two features: Pclass and Fare
X_train_vis = X_train[['Pclass', 'Fare']]
X_test_vis = X_test[['Pclass', 'Fare']]

# Train SVM on the 2D data
svm_model_vis = SVC(kernel='linear')
svm_model_vis.fit(X_train_vis, y_train)

# Create meshgrid for plotting decision boundary
x_min, x_max = X_train_vis['Pclass'].min() - 1, X_train_vis['Pclass'].max() + 1
y_min, y_max = X_train_vis['Fare'].min() - 1, X_train_vis['Fare'].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

# Predict the label for each point in the meshgrid
Z = svm_model_vis.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.75, cmap='coolwarm')
plt.scatter(X_train_vis['Pclass'], X_train_vis['Fare'], c=y_train, edgecolors='k', marker='o', label="Train data", cmap='coolwarm')
plt.scatter(X_test_vis['Pclass'], X_test_vis['Fare'], c=y_test, edgecolors='k', marker='x', label="Test data", cmap='coolwarm')
plt.title("SVM Decision Boundary with Pclass and Fare")
plt.xlabel('Pclass')
plt.ylabel('Fare')
plt.legend()
plt.show()
