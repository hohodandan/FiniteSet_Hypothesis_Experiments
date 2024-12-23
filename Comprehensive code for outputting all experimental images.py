import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import tracemalloc

# 映射函数定义
def mapping(n, a=1):
    w = n**a
    x = np.sin(n)
    y = np.cos(n)
    z = np.sqrt(n)
    return w, x, y, z

def mapping_4d(n, a=1):
    w = n**a
    x = np.sin(n)
    y = np.cos(n)
    z = np.sqrt(n)
    t = n  # 时间维度
    return w, x, y, z, t

# 实验1：几何验证
def geometric_test(k, a=1):
    n_values = np.arange(1, k + 1)
    w, x, y, z = mapping(n_values, a)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(x, y, z, c=n_values, cmap='viridis', marker='.')
    plt.colorbar(sc, label='Natural Numbers')
    ax.set_title(f'3D Mapping of Natural Numbers (k={k})')
    ax.set_xlabel('X Dimension')
    ax.set_ylabel('Y Dimension')
    ax.set_zlabel('Z Dimension')
    plt.show()

def visualize_4d_mapping(k):
    n_values = np.arange(1, k + 1)
    _, x, y, z, t = mapping_4d(n_values)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(x, y, z, c=t, cmap='plasma', marker='.')
    plt.colorbar(sc, label='Time Dimension')
    ax.set_title(f'4D Mapping of Natural Numbers (k={k})')
    ax.set_xlabel('X Dimension')
    ax.set_ylabel('Y Dimension')
    ax.set_zlabel('Z Dimension')
    plt.show()

# 实验2：性能测试
def performance_test(max_k):
    k_values = [10**3, 10**4, 10**5, max_k]
    time_results = []
    memory_results = []

    for k in k_values:
        start_time = time.time()
        tracemalloc.start()
        
        n_values = np.arange(1, k + 1)
        mapping(n_values)
        
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        time_results.append(time.time() - start_time)
        memory_results.append(peak / 1e6)  # 转换为MB

    # 性能图
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(k_values, time_results, 'b-o', label='Time')
    ax2.plot(k_values, memory_results, 'r-s', label='Memory')

    ax1.set_xlabel('k (Event Scale)')
    ax1.set_ylabel('Time (s)', color='b')
    ax2.set_ylabel('Memory (MB)', color='r')
    ax1.set_title('Performance Test')
    fig.tight_layout()
    plt.show()

# 实验3：数论验证（Goldbach 验证）
def goldbach_test(k):
    primes = [n for n in range(2, k) if all(n % d != 0 for d in range(2, int(np.sqrt(n)) + 1))]
    even_numbers = [n for n in range(4, k, 2)]
    verified = []

    for even in even_numbers:
        found = any(even - p in primes for p in primes)
        verified.append(found)

    success_rate = sum(verified) / len(even_numbers)
    print(f"Goldbach Conjecture Verification for k={k}: {success_rate * 100:.2f}%")

# 数值分布分析
def analyze_mapping_distribution(k):
    n_values = np.arange(1, k + 1)
    w, x, y, z = mapping(n_values)

    print("Distribution Analysis:")
    print(f"X Range: {np.min(x):.2f} to {np.max(x):.2f}")
    print(f"Y Range: {np.min(y):.2f} to {np.max(y):.2f}")
    print(f"Z Range: {np.min(z):.2f} to {np.max(z):.2f}")
    print(f"W Range: {np.min(w):.2f} to {np.max(w):.2f}")

    # 点分布密度
    density = len(n_values) / (np.max(z) - np.min(z))
    print(f"Point Density (Z Dimension): {density:.2f} points per unit")

# 主函数：运行所有实验
def main():
    print("Running Geometric Test...")
    geometric_test(1000)

    print("Running 4D Visualization...")
    visualize_4d_mapping(1000)

    print("Running Performance Test...")
    performance_test(50000)

    print("Running Goldbach Conjecture Test...")
    goldbach_test(1000)

    print("Running Distribution Analysis...")
    analyze_mapping_distribution(1000)

if __name__ == "__main__":
    main()


