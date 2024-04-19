import math

def smallest_pfactor(num):
    if num < 4:
        return num
    if num % 2 == 0:
        return 2
    if num % 3 == 0:
        return 3
    for i in range(5, math.isqrt(num), 6):
        if num % i == 0:
            return i
        if num % (i + 2) == 0:
            return i + 2
    return num

def distinct_pfactors(num):
    factors = []

    while num != 1:
        factor = smallest_pfactor(num)
        num = int(num / factor)
        if not factor in factors:
            factors.append(factor)
    return factors

def check_done(num):
    for i in range(4):
        if len(distinct_pfactors(num +  i)) != 4:
            return False
    return True

for i in range(1, 1000000):
    if check_done(i):
        print(i)
        break