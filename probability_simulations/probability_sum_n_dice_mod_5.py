import random
from itertools import product

def get_dice_roll():
    return random.randint(1, 6)

def simulate(num_dice, remainder):
    total = sum([get_dice_roll() for _ in range(num_dice)])
    return total % 5 == remainder

def run_simulaiton(num_dice, remainder):
    iterations = 1000000
    num_good_trials = 0
    for _ in range(iterations):
        if simulate(num_dice, remainder):
            num_good_trials += 1
    print("observed:", num_good_trials / iterations)
    print("expected:", (int(6 ** num_dice / 5) + (1 if remainder == num_dice % 5 else 0)) / (6 ** num_dice))
    print("expected extra:", (int(6 ** num_dice / 5) + 1) / (6 ** num_dice))
    print("expected not extra:", (int(6 ** num_dice / 5)) / (6 ** num_dice))

def calculate_all_possibilities(num_dice, remainder):
    dice_products = product([i for i in range(1, 6+1)], repeat=num_dice)

    num_products = 0
    num_good_products = 0
    for dice_product in dice_products:
        if sum(list(dice_product)) % 5 == remainder:
            num_good_products += 1
        num_products += 1
    return num_good_products / num_products

if __name__ == "__main__":
    num_dice = 10
    remainder = 0    

    print(calculate_all_possibilities(num_dice, remainder))

    # run_simulaiton(num_dice, remainder)