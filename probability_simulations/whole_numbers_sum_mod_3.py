import random
import math

def simulate_slow(k):
    numbers = list(range(1, (3 * k + 1) + 1)) 
    random.shuffle(numbers)

    total = 0
    for number in numbers:
        total += number
        if total % 3 == 0:
            return False        
    return True

def simulate(k):
    index_map = {
        1: 0,
        -1: 1,
        0: 2
    }
    counts = [k+1, k, k] # 1, -1, 0
    total = 0
    for _ in range(3 * k + 1):
        number = random.choices([1, -1, 0], weights=[counts[i] / sum(counts) for i in range(3)], k=1)[0]
        counts[index_map[number]] -= 1
        total += number
        if total % 3 == 0:
            return False
    return True


if __name__ == "__main__":
    k = 4
    iterations = 1000000

    good = 0
    for i in range(iterations):
        if simulate_slow(k):
            good += 1
    print("good / iterations", good / iterations)
    print("maybe actual", math.comb(3 * k, k) / (math.factorial(3 * k + 1) / math.factorial(k + 1) / math.factorial(k) / math.factorial(k)))