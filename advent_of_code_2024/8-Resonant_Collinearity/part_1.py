from collections import defaultdict
from itertools import combinations
import numpy as np

def get_antinode_positions(pair):
    position1, position2 = np.array(pair)
    # [0, 1], [0, 2] -> target: [0, 0] and [0, 3]
    # A, B -> B - A = [0, 1] -> target: A - (B - A) and B + (B - A) -> 2A - B and 2B - A
    return tuple(2 * position1 - position2), tuple(2 * position2 - position1)

with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

puzzle = [list(line) for line in lines]
PUZZLE_LENGTHS = (len(puzzle), len(puzzle[0]))

def in_puzzle(position, puzzle_lengths=PUZZLE_LENGTHS):
    return 0 <= position[0] < puzzle_lengths[0] and 0 <= position[1] < puzzle_lengths[1]

# all antinodes are the same, if an antinode from a frequency overlaps with an antinode from another frequency, it should count as one

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
        if in_puzzle(antinode_positions[0]):
            total_antinode_positions.add(antinode_positions[0])
        if in_puzzle(antinode_positions[1]):
            total_antinode_positions.add(antinode_positions[1])


print(len(total_antinode_positions))
print(total_antinode_positions)


