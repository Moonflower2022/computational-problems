import random

def simulate(num_bags, num_people):
    return len(set([random.randint(1, num_people) for _ in range(num_bags)]))

if __name__ == "__main__":
    num_bags = 20
    num_people = 20

    iterations = 1000000
    total_num_at_least_one = 0
    for _ in range(iterations):
        total_num_at_least_one += simulate(num_bags, num_people)

    print(total_num_at_least_one / iterations)