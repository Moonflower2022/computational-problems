import random
import numpy as np

def simulate(num_people, num_locations):
    locations = np.zeros(num_locations)

    for _ in range(num_people):
        locations[random.randint(0, num_locations - 1)] += 1

    return np.array([np.count_nonzero(locations == 0), np.count_nonzero(locations == 1), np.count_nonzero(locations > 1)])

if __name__ == "__main__":
    num_people = 3 # K in the problem
    num_locations = 2 # N in the problem


    counts = np.zeros(3)

    iterations = 100000
    for i in range(iterations):
        counts += simulate(num_people, num_locations)
    print(counts / iterations)