import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import make_scorer, roc_auc_score
import numpy as np

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Preprocessing

# Selecting Features and Target
features = ['Pclass', 'Age', 'Fare']
target = 'Survived'

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(), inplace=True)

# Extract Features and Target
X = titanic_df[features]
y = titanic_df[target]

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Logistic Regression Model
logreg = LogisticRegression()

# Cross-validation with 5 folds
cv_scores = cross_val_score(logreg, X_scaled, y, cv=5, scoring='accuracy')

# Cross-validation ROC-AUC
roc_auc_scorer = make_scorer(roc_auc_score, needs_proba=True)
cv_roc_auc_scores = cross_val_score(logreg, X_scaled, y, cv=5, scoring=roc_auc_scorer)

# Results
print(f"Cross-Validated Accuracy Scores: {cv_scores}")
print(f"Mean Accuracy: {np.mean(cv_scores):.2f}")
print(f"Cross-Validated ROC-AUC Scores: {cv_roc_auc_scores}")
print(f"Mean ROC-AUC: {np.mean(cv_roc_auc_scores):.2f}")
