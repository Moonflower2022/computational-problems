import math

def is_prime(num):
    if num < 4:
        return num > 1
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, math.isqrt(num) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def is_prime_other(num):
    if num < 4:
        return num > 1
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def shift(num, shifts):
    if shifts == 0:
        return num
    str_representation = str(num)
    return int(str_representation[-shifts:] + str_representation[:-shifts])

total = 0

for i in range(1, 1_000_000):
    for j in range(len(str(i))):
        if not is_prime(shift(i, j)):
            break
        if j == len(str(i)) - 1:
            total += 1

print(total)