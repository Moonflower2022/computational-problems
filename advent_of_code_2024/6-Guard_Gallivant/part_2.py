def in_puzzle(puzzle, y, x):
    return 0 <= y < len(puzzle) and 0 <= x < len(puzzle[0])

def get_new_direction(directions_values, current_direction_index):
    return directions_values[(current_direction_index + 1) % 4], (current_direction_index + 1) % 4

def get_next_location(current_location, current_direction):
    return [
        current_location[0] + current_direction[0],
        current_location[1] + current_direction[1],
    ]

def get_hashed_state(direction, location):
    return (location[0], location[1], direction[0], direction[1])

def will_loop(puzzle, starting_direction, starting_location):
    current_direction = starting_direction[:]
    current_location = starting_location[:]
    states = {get_hashed_state(current_direction, current_location)}

    directions_values = list(directions.values())
    current_direction_index = directions_values.index(starting_direction)

    while True:
        next_y, next_x = get_next_location(current_location, current_direction)
 
        if not in_puzzle(puzzle, next_y, next_x):
            return False
        if puzzle[next_y][next_x] == "#":
            current_direction, current_direction_index = get_new_direction(directions_values, current_direction_index)
            continue
        current_location = [next_y, next_x]
        if get_hashed_state(current_direction, current_location) in states:
            return True
        states.add(get_hashed_state(current_direction, current_location))

import os

script_dir = os.path.dirname(os.path.abspath(__file__))  # get the directory of the current script
file_path = os.path.join(script_dir, "puzzle_input.txt")

with open(file_path, "r") as input_file:
    lines = input_file.read().split("\n")

puzzle = [list(line) for line in lines]
# things should be in y, x
directions = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

for y, row in enumerate(puzzle):
    for x, element in enumerate(row):
        if element in directions.keys():
            direction = directions[element]
            location = [y, x]

def convert_to_string(puzzle):
    string_puzzle = ""
    for row in puzzle:
        for element in row:
            string_puzzle += element
        string_puzzle += "\n"

    return string_puzzle

num_loops = 0

i = 0
print(f"{len(puzzle)}x{len(puzzle[0])} puzzle")
for y, row in enumerate(puzzle):
    for x, element in enumerate(row):
        print(f"{i} positions checked", end="\r")
        if puzzle[y][x] == ".":
            puzzle[y][x] = "#"
            if will_loop(puzzle, direction, location):
                num_loops += 1
                # puzzle[y][x] = "O"
                # print(convert_to_string(puzzle))
            puzzle[y][x] = "."
            i += 1

print(f"{i} positions checked")
print(num_loops)