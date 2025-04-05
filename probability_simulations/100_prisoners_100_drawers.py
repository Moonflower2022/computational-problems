import random
import numpy as np
import matplotlib.pyplot as plt

def get_max_loop_length(n):
    order = list(range(n))
    random.shuffle(order)

    lengths = []

    unchecked = list(range(n))
    while len(unchecked) > 0:
        original_to_check = unchecked[-1]
        to_check = unchecked[-1]
        unchecked.remove(to_check)
        to_check = order[to_check]
        i = 0
        while True:
            i += 1
            if to_check == original_to_check:
                lengths.append(i) 
                break
            else:
                unchecked.remove(to_check)
                to_check = order[to_check]

    return max(lengths)

if __name__ == '__main__':
    n = 100

    iterations = int(1e5)

    total_max_loop_length_equals_j = np.zeros(n)
    for i in range(iterations):
        max_loop_length = get_max_loop_length(n)
        for j in range(n):
            total_max_loop_length_equals_j[j] += 1 if max_loop_length == j + 1 else 0
    print(total_max_loop_length_equals_j/iterations)

    plt.bar(range(n), total_max_loop_length_equals_j)
    plt.show()
