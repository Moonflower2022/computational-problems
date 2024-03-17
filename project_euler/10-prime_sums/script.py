import math

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

total = 0
threshold = 2_000_000

for i in range(2, threshold):
  if is_prime(i):
    total += i

print(total)