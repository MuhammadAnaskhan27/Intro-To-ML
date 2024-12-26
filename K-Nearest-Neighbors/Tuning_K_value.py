import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Preprocessing

# Select Features and Target
features = ['Age','Pclass','Fare']
target = 'Survived'

# Handle the missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(), inplace=True)

# Extract Features and Target
x = titanic_df[features]
y = titanic_df[target]

# Splitting data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Standardize Features 
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Testing different values of k
k_values = range(1,21)
accuracies = []

for k in k_values:
    # knn model
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train_scaled,y_train)
    # prediction on test set
    y_pred = knn.predict(x_test_scaled)
    accuracy = accuracy_score(y_test,y_pred)
    accuracies.append(accuracy)

# Plotting the results
plt.figure(figsize=(10,6))
plt.plot(k_values,accuracies,marker='o',linestyle='-',color='blue')
plt.title("Accuracy vs. k-value for k-NN")
plt.xlabel("k-value")
plt.ylabel("Accuracy")
plt.grid()
plt.show()

# Find the optimal k-value
optimal_k = k_values[accuracies.index(max(accuracies))]
print(f"The optimal k-value is: {optimal_k}")
print(f"The highest accuracy achieved is: {max(accuracies):.2f}")
