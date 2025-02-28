import random

def get_num_aces(num_draws):
    num_aces_left = 4
    num_aces = 0
    for _ in range(num_draws):
        if random.random() < 1 / 13:

            num_aces_left -= 1
            num_aces += 1
            if num_aces == 0:
                break
    return num_aces



if __name__ == "__main__":
    iterations = 10000000

    num_draws = 5
    total_num_aces = 0

    for i in range(iterations):
        total_num_aces += get_num_aces(num_draws)

    print(total_num_aces / iterations)