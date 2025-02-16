import random

def simulate(num_people, num_plane_seats, p):
    return sum([1 if random.random() < p else 0 for _ in range(num_people)]) <= num_plane_seats

if __name__ == "__main__":
    num_people = 110
    num_plane_seats = 100
    p = 0.9

    iterations = 1000000
    num_good = 0
    for _ in range(iterations):
        if simulate(num_people, num_plane_seats, p):
            num_good += 1
    print(num_good / iterations)

