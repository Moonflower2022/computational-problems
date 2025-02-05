from collections import defaultdict

def get_update(stone_number):
    if stone_number == 0:
        return [1]
    if len(str(stone_number)) % 2 == 0:
        halfway_point = int(len(str(stone_number)) / 2)
        return [int(str(stone_number)[:halfway_point]), int(str(stone_number)[halfway_point:])]
    return [stone_number * 2024]

def update_stones(stone_numbers):
    new_stone_numbers = defaultdict(int)
    for stone_number, count in stone_numbers.items():
        update = get_update(stone_number)
        if len(update) == 2:
            new_stone_numbers[update[0]] += count
            new_stone_numbers[update[1]] += count
        else: # len(update) == 1
            new_stone_numbers[update[0]] += count
    return new_stone_numbers

import os

script_dir = os.path.dirname(
    os.path.abspath(__file__)
)  # get the directory of the current script
file_path = os.path.join(script_dir, "puzzle_input.txt")

with open(file_path, "r") as input_file:
    number_strings = input_file.read().split(" ")

stone_numbers = {int(number_string): 1 for number_string in number_strings}

num_blinks = 75

for _ in range(num_blinks):
    stone_numbers = update_stones(stone_numbers)

print(sum(count for count in stone_numbers.values()))