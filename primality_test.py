from math import isqrt
import matplotlib.pyplot as plt
import time
import numpy as np
import math

def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_optimized(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

times = []
optimized_times = []
nums = list(range(int(1e19), int(1e22), int(1e19)))

total_start_time = time.time()

for num in nums:
    start_time = time.time()
    is_prime(num)
    times.append(time.time() - start_time)
    start_time = time.time()
    is_prime_optimized(num)
    optimized_times.append(time.time() - start_time)

print("Runtime (s):", time.time() - total_start_time)

plt.plot(nums, times, label='is_prime')
plt.plot(nums, optimized_times, label='is_prime_optimized')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (s)')
plt.title('Performance of is_prime vs is_prime_optimized')
plt.legend()
plt.show()
