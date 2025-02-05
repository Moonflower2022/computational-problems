def get_update(stone_number):
    if stone_number == 0:
        return [1]
    if len(str(stone_number)) % 2 == 0:
        halfway_point = int(len(str(stone_number)) / 2)
        return [int(str(stone_number)[:halfway_point]), int(str(stone_number)[halfway_point:])]
    return [stone_number * 2024]

def update_stones(stone_numbers):
    new_stone_numbers = []
    for stone_number in stone_numbers:
        new_stone_numbers += get_update(stone_number)
    return new_stone_numbers

import os

script_dir = os.path.dirname(
    os.path.abspath(__file__)
)  # get the directory of the current script
file_path = os.path.join(script_dir, "puzzle_input.txt")

with open(file_path, "r") as input_file:
    number_strings = input_file.read().split(" ")

stone_numbers = [int(number_string) for number_string in number_strings]

num_blinks = 25

for _ in range(num_blinks):
    stone_numbers = update_stones(stone_numbers)

print(len(stone_numbers))