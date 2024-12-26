from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load sample data (e.g., house prices)
X = [[1200], [1400], [1600], [1800], [2000]]  # Square footage
y = [200000, 250000, 300000, 350000, 400000]  # Prices

# Train model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# R-squared score
print("R-squared:", r2_score(y, y_pred))


import matplotlib.pyplot as plt

plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title("Linear Regression: House Prices")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()