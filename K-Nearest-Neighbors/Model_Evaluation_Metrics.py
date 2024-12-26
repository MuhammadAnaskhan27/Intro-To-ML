import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,recall_score,f1_score,precision_score,roc_auc_score,confusion_matrix,classification_report
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

# loading titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Preprocessing

# Selecting Features and target
features = ['Pclass','Age','Fare']
target = 'Survived'

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(),inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(),inplace=True)

# Extract Features and target
x = titanic_df[features]
y = titanic_df[target]

# Splitting dataset into training and testing sets
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Standardization
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Logistic Regression Model
logreg = LogisticRegression()
logreg.fit(x_train_scaled,y_train)

# Predict on test set
y_pred = logreg.predict(x_test_scaled)
y_pred_prob = logreg.predict_proba(x_test_scaled)[:,1]

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Precision
precision = precision_score(y_test, y_pred)
print(f"Precision: {precision:.2f}")

# Recall
recall = recall_score(y_test, y_pred)
print(f"Recall: {recall:.2f}")

# F1-Score
f1 = f1_score(y_test, y_pred)
print(f"F1-Score: {f1:.2f}")

# ROC-AUC
roc_auc = roc_auc_score(y_test, y_pred_prob)
print(f"ROC-AUC: {roc_auc:.2f}")

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Classification Report
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)

# Roc Curve Plot
fpr,tpr,thresholds = roc_curve(y_test,y_pred_prob)

plt.figure(figsize=(10,6))
plt.plot(fpr,tpr,color='blue',label='ROC Curve')
plt.plot([0,1],[0,1],color='gray',linestyle='--')
plt.title("ROC Curve")
plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate (TPR)")
plt.legend()
plt.show()