import numpy as np  # Import numpy module
import time
import tracemalloc
import matplotlib.pyplot as plt

# Function: Map natural numbers to 3D space
def map_to_3d(n, k):
    x = np.sin(2 * np.pi * n / k) * n
    y = np.cos(2 * np.pi * n / k) * n
    z = n / k
    return x, y, z

# Performance test function
def performance_test(max_k):
    k_values = [100, 1000, 5000, 10000, 50000]
    time_results = []
    memory_results = []

    for k in k_values:
        n_values = np.arange(1, k + 1)

        # Start memory tracking
        tracemalloc.start()
        start_time = time.time()

        # Perform the mapping
        x_vals, y_vals, z_vals = map_to_3d(n_values, k)

        # Stop memory tracking
        current, peak = tracemalloc.get_traced_memory()
        end_time = time.time()

        # Record time and memory
        time_results.append(end_time - start_time)
        memory_results.append(peak / (1024 * 1024))  # Convert to MB

        tracemalloc.stop()

    # Return results
    return k_values, time_results, memory_results

# Performance test
k_values, time_results, memory_results = performance_test(50000)

# Plot the results
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('k (Event Scale)')
ax1.set_ylabel('Time (s)', color='tab:blue')
ax1.plot(k_values, time_results, '-o', label='Execution Time', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Memory (MB)', color='tab:red')
ax2.plot(k_values, memory_results, '-s', label='Memory Usage', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

fig.tight_layout()
plt.title('Performance Analysis: Time and Memory Usage')
plt.show()


