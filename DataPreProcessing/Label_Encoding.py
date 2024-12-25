from sklearn.preprocessing import LabelEncoder

# Categories
animals = ["Dog", "Cat", "Fish", "Dog", "Fish", "Cat"]

# Create the encoder
label_encoder = LabelEncoder()

# Fit and transform
encoded_labels = label_encoder.fit_transform(animals)

print("Original Categories:", animals)
print("Label Encoded Values:", encoded_labels)
