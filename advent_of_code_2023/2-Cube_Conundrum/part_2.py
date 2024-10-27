from part_1 import parse_game_data
from math import prod

def get_minimum_cubes(cube_combinations):
    minimum_cubes = {"red": 0, "green": 0, "blue": 0}
    colors = ["red", "green", "blue"]
    for cubes in cube_combinations:
        for color in colors:
            if color in cubes:
                minimum_cubes[color] = max(minimum_cubes[color], cubes[color])

    return minimum_cubes

def get_cube_power(cubes):
    return prod(cubes.values())

if __name__ == '__main__':
    with open("puzzle_input.txt", "r") as file:
        games = [parse_game_data(game_raw)[1] for game_raw in file.read().split("\n")]

    total = sum([get_cube_power(get_minimum_cubes(cube_combinations)) for cube_combinations in games])

    print(total)
    