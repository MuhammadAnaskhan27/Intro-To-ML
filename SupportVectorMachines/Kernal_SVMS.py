import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Preprocessing
features = ['Pclass', 'Age', 'Fare']
target = 'Survived'

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(), inplace=True)

# Extract Features and Target
X = titanic_df[features]
y = titanic_df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train SVM models with different kernels
kernels = ['linear', 'poly', 'rbf']
accuracies = []

for kernel in kernels:
    # Create and train the SVM model with the specified kernel
    svm_model = SVC(kernel=kernel)
    svm_model.fit(X_train_scaled, y_train)

    # Predict on the test set
    y_pred = svm_model.predict(X_test_scaled)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f"Accuracy with {kernel} kernel: {accuracy:.2f}")

# Compare performance of different kernels
plt.figure(figsize=(8, 6))
plt.bar(kernels, accuracies, color=['blue', 'green', 'red'])
plt.xlabel('Kernel Type')
plt.ylabel('Accuracy')
plt.title('SVM Model Accuracy with Different Kernels')
plt.show()
