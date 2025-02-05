# trail from 0 to 9
# no diagonal
# find all 0s; score is # of 9s that can be reached from there

import os

script_dir = os.path.dirname(
    os.path.abspath(__file__)
)  # get the directory of the current script
file_path = os.path.join(script_dir, "puzzle_input.txt")

with open(file_path, "r") as input_file:
    lines = input_file.read().split("\n")

puzzle = [list(line) for line in lines]
PUZZLE_LENGTHS = (len(puzzle), len(puzzle[0]))


def in_puzzle(position, puzzle_lengths=PUZZLE_LENGTHS):
    return 0 <= position[0] < puzzle_lengths[0] and 0 <= position[1] < puzzle_lengths[1]


def neighbor_is_possible(position, neighbor_position, puzzle=puzzle):
    return (
        in_puzzle(neighbor_position)
        and int(puzzle[position[0]][position[1]]) + 1
        == int(puzzle[neighbor_position[0]][neighbor_position[1]])
    )


def get_possible_neighbors(position):
    differences = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    possible_neighbors = []

    for difference in differences:
        neighbor = (position[0] + difference[0], position[1] + difference[1])
        if neighbor_is_possible(position, neighbor):
            possible_neighbors.append(neighbor)
    return possible_neighbors


def get_score(trail_head_position, puzzle=puzzle):
    current_positions = [trail_head_position]
    while not all(puzzle[position[0]][position[1]] == "9" for position in current_positions):
        new_positions = []
        for position in current_positions:
            if puzzle[position[0]][position[1]] == "9":
                new_positions.append(position)
            else:
                new_positions += get_possible_neighbors(position)
        current_positions = new_positions

    return len(current_positions)

total_score = 0

for y, row in enumerate(puzzle):
    for x, element in enumerate(row):
        if element == "0":
            print(get_score((y, x), puzzle))
            total_score += get_score((y, x), puzzle)

print(total_score)
