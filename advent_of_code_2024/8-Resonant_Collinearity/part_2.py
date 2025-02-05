from collections import defaultdict
from itertools import combinations
import numpy as np

with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

puzzle = [list(line) for line in lines]
PUZZLE_LENGTHS = (len(puzzle), len(puzzle[0]))

# all antinodes are the same, if an antinode from a frequency overlaps with an antinode from another frequency, it should count as one

def in_puzzle(position, puzzle_lengths=PUZZLE_LENGTHS):
    return 0 <= position[0] < puzzle_lengths[0] and 0 <= position[1] < puzzle_lengths[1]

def get_antinode_positions(pair):
    # [0, 1], [0, 2] -> target: [0, 0] and [0, 3]
    # A, B -> B - A = [0, 1] -> target: A - (B - A) and B + (B - A) -> 2A - B and 2B - A
    position1, position2 = np.array(pair)
    difference = position2 - position1
    antinode_positions = []
    i = 0
    while in_puzzle(position1 - i * difference):
        antinode_positions.append(tuple(position1 - i * difference))
        i += 1
    i = 0
    while in_puzzle(position2 + i * difference):
        antinode_positions.append(tuple(position2 + i * difference))
        i += 1
    return antinode_positions

antenna_positions = defaultdict(list)

for y, row in enumerate(puzzle):
    for x, element in enumerate(row):
        if element != ".":
            antenna_positions[element].append((y, x))

total_antinode_positions = set()

for frequency in antenna_positions.keys():
    pairs = combinations(antenna_positions[frequency], r=2)
    for pair in pairs:
        antinode_positions = get_antinode_positions(pair)
        for antinode_position in antinode_positions:
            total_antinode_positions.add(antinode_position)

print(len(total_antinode_positions))
# print(total_antinode_positions)
