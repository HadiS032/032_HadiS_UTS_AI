import numpy as np

inputs = [2.1, 1.5, 3.0, 1.8, 3.4, 2.6, 1.0, 4.0, 2.5, 3.6]
weights = [
    [0.5, 1.2, 3.2, 2.4, 4.2, 3.6, 1.8, 2.6, 3.4, 0.8],
    [3.2, 1.6, 2.5, 4.1, 3.9, 0.6, 3.1, 2.7, 1.9, 0.4],
    [2.4, 1.5, 1.0, 2.6, 3.2, 1.5, 4.5, 2.9, 1.8, 2.5],
    [4.1, 2.0, 1.4, 3.1, 0.4, 2.7, 1.9, 3.4, 4.0, 1.3],
    [1.8, 4.3, 3.1, 2.5, 1.6, 3.1, 4.5, 2.7, 0.7, 3.8],
]

biases = [3.4, 1.5, 2.0, 2.1, 1.0]

outputs = np.dot(weights, inputs) + biases
print(outputs)