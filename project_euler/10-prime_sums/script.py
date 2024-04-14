import time
import math

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


threshold = 6_000_000
start_time = time.time()

total = sum(n for n in range(2, threshold) if is_prime(n))

print("Running time (s):", time.time() - start_time)
print(f"Sum of primes under {threshold}:", total)