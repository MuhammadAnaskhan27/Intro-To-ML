from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Categories
animals = np.array(["Dog", "Cat", "Fish", "Dog", "Fish", "Cat"]).reshape(-1, 1)

# Create the encoder
one_hot_encoder = OneHotEncoder()

# Fit and transform
encoded_one_hot = one_hot_encoder.fit_transform(animals)

print("Original Categories:", animals.flatten())
print("One-Hot Encoded Matrix:\n", encoded_one_hot)
