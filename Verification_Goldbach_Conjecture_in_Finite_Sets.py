import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

# Set matplotlib to use English fonts
matplotlib.rcParams['font.sans-serif'] = ['Arial']  # Use Arial font
matplotlib.rcParams['axes.unicode_minus'] = False  # Solve the issue with displaying minus sign '-'

# Generate all prime numbers less than k using the Sieve of Eratosthenes
def sieve_of_eratosthenes(k):
    sieve = [True] * (k+1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for start in range(2, int(k**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, k+1, start):
                sieve[i] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return set(primes)  # Use a set to store primes for faster lookup

# Goldbach Conjecture verification: For every even number 2n in the set {1, 2, ..., k},
# find two primes p1 and p2 such that p1 + p2 = 2n
def goldbach_conjecture(k, primes):
    success_count = 0
    # Iterate over the even numbers in the set
    for n in range(4, k+1, 2):  # Start from 4, step by 2
        found = False
        # For each even number 2n, check if it can be expressed as the sum of two primes
        for p1 in primes:
            p2 = n - p1
            if p2 >= 2 and p2 in primes:  # If p2 is a prime number
                found = True
                break
        if found:
            success_count += 1
    # Calculate the success rate
    success_rate = (success_count / (k//2)) * 100  # k//2 is the number of even numbers
    return success_rate

# Choose different k values for validation
k_values = [1000, 10000, 100000, 1000000]
success_rates = []

# Pre-generate primes
max_k = max(k_values)
primes = sieve_of_eratosthenes(max_k)

# Record the start time for each k
start_time = time.time()

for k in k_values:
    success_rate = goldbach_conjecture(k, primes)
    success_rates.append(success_rate)
    print(f"Set size k = {k}: Validation success rate = {success_rate:.2f}%")

# Print the results
print("\nGoldbach Conjecture Validation Results:")
for k, success_rate in zip(k_values, success_rates):
    print(f"Set size k = {k}: Validation success rate = {success_rate:.2f}%")

# Plot the success rate graph
plt.plot(k_values, success_rates, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)
plt.title("Goldbach Conjecture Validation Success Rate")
plt.xlabel("Set size k")
plt.ylabel("Validation success rate (%)")
plt.grid(True)
plt.show()

# Print the execution time
end_time = time.time()
print(f"\nProgram execution time: {end_time - start_time:.2f} seconds")

