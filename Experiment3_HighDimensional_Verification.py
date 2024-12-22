import numpy as np  # Import numpy module
import matplotlib.pyplot as plt

# Function: Map natural numbers to high-dimensional space
def map_to_high_dim(n, k):
    x = np.sin(2 * np.pi * n / k) * n
    y = np.cos(2 * np.pi * n / k) * n
    z = n / k
    return x, y, z

# Set parameters
k = 100  # Maximum natural number for the mapping
n_values = np.arange(1, k + 1)  # Range of natural numbers

# Perform the mapping
x_values, y_values, z_values = map_to_high_dim(n_values, k)

# Plot 3D graph
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x_values, y_values, z_values, c='b', marker='o', s=10, alpha=0.7)
ax.set_title(f'Mapping of Natural Numbers (k={k})')
ax.set_xlabel('X Dimension')
ax.set_ylabel('Y Dimension')
ax.set_zlabel('Z Dimension')

plt.show()
