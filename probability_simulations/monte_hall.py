import random

def simulate(N=7, K=3):
    doors = list(range(N))
    car_door = random.choice(doors)

    my_door = random.choice(doors)

    doors.remove(my_door)
    if not my_door == car_door:
        doors.remove(car_door)

    for i in range(K):
        doors.remove(random.choice(doors))
    if not my_door == car_door:
        doors.append(car_door)

    return random.choice(doors) == car_door


if __name__ == "__main__":
    N = 8
    K = 3
    iterations = 1000000

    correct = 0

    for i in range(iterations):
        if simulate(N=N, K=K):
            correct += 1

    print(correct / iterations)

    # expected outcome is ≈ (n - 1) / n / (n - k - 1)