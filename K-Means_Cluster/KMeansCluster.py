from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load Titanic Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Preprocessing

# Selecting features and target
features = ['Age','Pclass','Fare']

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(),inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(),inplace=True)

# Extract features and target 
x = titanic_df[features]

# Standardizing the data
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# K-Means Cluster
km = KMeans(n_clusters=3,random_state=42)
km.fit(x_scaled)

# Add the cluster labels to the original dataframe
titanic_df['Cluster'] = km.labels_

# Visualize the clusters (using 2D plot for simplicity)
plt.figure(figsize=(10, 6))

# Create a scatter plot of the clusters
plt.scatter(titanic_df['Age'], titanic_df['Fare'], c=titanic_df['Cluster'], cmap='viridis', alpha=0.6)
plt.title("k-Means Clustering of Titanic Dataset")
plt.xlabel('Age')
plt.ylabel('Fare')
plt.colorbar(label='Cluster')
plt.show()

# Optionally, print the centroids of the clusters
print("Cluster Centers (Centroids):")
print(km.cluster_centers_)


