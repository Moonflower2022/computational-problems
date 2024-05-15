import random


def user_input():
    print("How many faces per dice? ")
    dice_faces = int(input())
    print("Number of dice? ")
    dice_num = int(input())
    print("How many times to simulate? ")
    iterations = int(input())
    total_thing = 0

    for i in range(iterations):
        dice_results = []
        for i in range(dice_num):
            dice_results.append(random.randint(1, dice_faces))
        total_thing = total_thing + max(*dice_results)
    print(total_thing/iterations)
    user_input()


user_input()
