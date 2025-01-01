import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Load Titanic Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Data Preprocessing
# Selecting features for clustering
features = ['Age', 'Fare','Pclass']

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df['Fare'].fillna(titanic_df['Fare'].median(), inplace=True)

# Extract features for clustering
X = titanic_df[features]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Hierarchical Clustering
# Generate the linkage matrix
linkage_matrix = linkage(X_scaled, method='ward')

# Plot the dendrogram
plt.figure(figsize=(12, 6))
dendrogram(linkage_matrix)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

# Agglomerative Clustering
# Choose the number of clusters based on the dendrogram
n_clusters = 3
hierarchical_clustering = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
titanic_df['Cluster'] = hierarchical_clustering.fit_predict(X_scaled)

# Visualize Clusters
plt.figure(figsize=(10, 6))
plt.scatter(titanic_df['Age'], titanic_df['Fare'], c=titanic_df['Cluster'], cmap='viridis', alpha=0.6)
plt.title(f'Agglomerative Clustering with {n_clusters} Clusters')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.colorbar(label='Cluster')
plt.show()
