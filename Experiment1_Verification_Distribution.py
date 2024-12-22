import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function: Map natural numbers to 3D space
def map_to_3d(n, k):
    x = np.sin(2 * np.pi * n / k) * n
    y = np.cos(2 * np.pi * n / k) * n
    z = n / k
    return x, y, z

# Parameters
k = 10000  # Set size
n_values = np.arange(1, k + 1)

# Mapping
x_vals, y_vals, z_vals = map_to_3d(n_values, k)

# Plot 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_vals, y_vals, z_vals, c=z_vals, cmap='viridis', s=1)

ax.set_title(f'Mapping of Natural Numbers (k={k})')
ax.set_xlabel('X Dimension')
ax.set_ylabel('Y Dimension')
ax.set_zlabel('Z Dimension')

plt.show()
