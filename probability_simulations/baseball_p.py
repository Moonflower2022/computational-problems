import random
from math import comb

def simulate(n, p):
    a_wins = 0
    b_wins = 0
    while a_wins < n and b_wins < n:
        if random.random() < p:
            a_wins += 1
        else:
            b_wins += 1

    return a_wins == n

if __name__ == "__main__":
    n = 4
    p = 0.6

    iterations = 1000000
    total_good = 0
    for i in range(iterations):
        if simulate(n, p):
            total_good += 1
    print(total_good / iterations)
    a = p ** n
    b = p ** n * (1 - p) * comb(n, 1)
    c = p ** n * (1 - p) ** 2 * comb(n + 1, 2)
    d = p ** n * (1 - p) ** 3 * comb(n + 2, 3)
    print("should be:", a+b+c+d)
