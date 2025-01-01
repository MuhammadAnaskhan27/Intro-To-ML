import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN, KMeans

# Load Titanic Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Preprocessing
# Selecting features for clustering
features = ['Age', 'Fare']

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(), inplace=True)

# Extract features for clustering
X = titanic_df[features]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)  # Parameters: eps (radius), min_samples (minimum points)
titanic_df['DBSCAN_Cluster'] = dbscan.fit_predict(X_scaled)

# Visualize DBSCAN Clusters
plt.figure(figsize=(10, 6))
plt.scatter(titanic_df['Age'], titanic_df['Fare'], c=titanic_df['DBSCAN_Cluster'], cmap='viridis', alpha=0.6)
plt.title("DBSCAN Clustering")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.colorbar(label='Cluster')
plt.show()

# Apply k-means for comparison
kmeans = KMeans(n_clusters=3, random_state=42)
titanic_df['KMeans_Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize k-means Clusters
plt.figure(figsize=(10, 6))
plt.scatter(titanic_df['Age'], titanic_df['Fare'], c=titanic_df['KMeans_Cluster'], cmap='viridis', alpha=0.6)
plt.title("k-Means Clustering")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.colorbar(label='Cluster')
plt.show()
