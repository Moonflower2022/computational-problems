import time
import math
import multiprocessing as mp

def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def prime_sum(arr):
    return sum(n for n in arr if is_prime(n))

if __name__ == '__main__':
    threshold = 6_000_000
    batch_size = 500_000
    start_time = time.time()

    with mp.Pool(processes=12) as pool:
        total = sum(pool.map(prime_sum, [list(range(6_000_000))[x:x+batch_size] for x in range(batch_size, threshold, batch_size)]))

    print("Running time (s):", time.time() - start_time)
    print(f"Sum of primes under {threshold}:", total)