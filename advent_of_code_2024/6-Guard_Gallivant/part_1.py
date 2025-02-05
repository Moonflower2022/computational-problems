def in_puzzle(puzzle, y, x):
    return 0 <= y < len(puzzle) and 0 <= x < len(puzzle[0])


def get_new_direction(directions, current_direction_index):
    return list(directions.values())[(current_direction_index + 1) % 4], (current_direction_index + 1) % 4


def get_next_location(current_location, current_direction):
    return [
        current_location[0] + current_direction[0],
        current_location[1] + current_direction[1],
    ]


with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

puzzle = [list(line) for line in lines]
# things should be in y, x
directions = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

for y, row in enumerate(puzzle):
    for x, element in enumerate(row):
        if element in directions.keys():
            current_direction = directions[element]
            current_direction_index = list(directions.keys()).index(element)
            current_location = [y, x]
            locations = {f"{y},{x}"}

while True:
    next_y, next_x = get_next_location(current_location, current_direction)
    print(current_location)

    if not in_puzzle(puzzle, next_y, next_x):
        break
    if puzzle[next_y][next_x] == "#":
        # hits # and then goes through
        current_direction, current_direction_index = get_new_direction(directions, current_direction_index)
    current_location = get_next_location(current_location, current_direction)
    next_y, next_x = current_location
    locations.add(f"{next_y},{next_x}")

print(len(locations))
