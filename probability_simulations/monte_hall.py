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

    return car_door == my_door # random.choice(doors) == car_door


        



if __name__ == "__main__":
    N = 7
    K = 3
    iterations = 100000

    correct = 0

    for i in range(iterations):
        if simulate(N=N, K=K):
            correct += 1

    print(correct / iterations)