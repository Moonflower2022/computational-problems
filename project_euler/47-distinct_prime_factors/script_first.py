import math
        
def smallest_pfactor(num):
    if num < 4:
        return num
    if num % 2 == 0:
        return 2
    if num % 3 == 0:
        return 3
    for i in range(5, math.isqrt(num) + 1, 6):
        if num % i == 0:
            return i
        if num % (i + 2) == 0:
            return i + 2
    return num

def distinct_pfactors(num):
    ret = []
    while num != 1:
        factor = smallest_pfactor(num)
        num = int(num/factor)
        if not factor in ret:
            ret.append(factor)
    return ret

def arrays_different(arr1, arr2):
    for element in arr1:
        if element in arr2:
            return False
    return True

def check_done(num):
    if len(distinct_pfactors(num)) != 4:
        return False
    for i in range(1, 4):
        if len(distinct_pfactors(num + i)) != 4 or not arrays_different(distinct_pfactors(num + i - 1), distinct_pfactors(num + i)):
            return False
    return True

for i in range(1, 10000000):
    if check_done(i):
        print(i)
