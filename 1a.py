import numpy as np

inputs = [2.1, 1.5, 3.0, 1.8, 3.4, 2.6, 1.0, 4.0, 2.5, 3.6]
weights = [3.0, 2.6, 1.0, 4.2, 3.2, 1.8, 2.4, 3.5, 2.8, 2.0]

bias = 4.5

outputs = np.dot(weights, inputs) + bias
print(outputs)
