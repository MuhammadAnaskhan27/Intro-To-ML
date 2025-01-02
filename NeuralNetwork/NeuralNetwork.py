import numpy as np

# Sigmoid Activation Function and its Derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network Class
class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the weights and biases
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)  # Random initialization
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))

    def forward(self, X):
        # Forward propagation
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = sigmoid(self.final_input)
        return self.final_output

    def backward(self, X, y, learning_rate):
        # Compute error
        error = y - self.final_output
        
        # Backpropagation
        d_output = error * sigmoid_derivative(self.final_output)
        error_hidden = d_output.dot(self.weights_hidden_output.T)
        d_hidden = error_hidden * sigmoid_derivative(self.hidden_output)
        
        # Update weights and biases using gradient descent
        self.weights_hidden_output += self.hidden_output.T.dot(d_output) * learning_rate
        self.bias_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += X.T.dot(d_hidden) * learning_rate
        self.bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        # Train the neural network
        for epoch in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)
            if epoch % 1000 == 0:  # Print the loss every 1000 iterations
                loss = np.mean(np.square(y - self.final_output))  # Mean Squared Error Loss
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Example usage
if __name__ == "__main__":
    # XOR Problem (for illustration)
    # Input (XOR inputs)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # Output (XOR outputs)
    y = np.array([[0], [1], [1], [0]])

    # Define and train the neural network
    input_size = 2  # Two input neurons
    hidden_size = 4  # Four neurons in the hidden layer
    output_size = 1  # One output neuron
    nn = SimpleNN(input_size, hidden_size, output_size)
    
    # Train the neural network
    nn.train(X, y, epochs=10000, learning_rate=0.1)
    
    # Test the trained neural network
    predictions = nn.forward(X)
    print("\nPredictions:")
    print(predictions)
