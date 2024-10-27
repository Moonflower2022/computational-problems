import re
from collections import defaultdict

def parse_game_data(data):
    # Regular expression to match the game ID and the list of combinations
    game_pattern = re.compile(r"Game (\d+): (.*)")

    # Match the pattern to extract the game ID and the list of combinations
    match = game_pattern.match(data)
    if match:
        game_id = int(match.group(1))  # Extract the game number (ID)
        combinations = match.group(2)  # Extract the combinations part

        # Split the combinations by semicolons
        combination_list = combinations.split(";")

        # Create a list to hold the parsed dictionaries for this game
        parsed_combinations = []

        for comb in combination_list:
            # Split each combination by commas and create a dictionary
            comb_dict = defaultdict(int)
            for part in comb.split(","):
                part = part.strip()
                # Extract the quantity and color
                quantity, color = part.split()
                comb_dict[color] = int(quantity)

            parsed_combinations.append(dict(comb_dict))

    return [game_id, parsed_combinations]


def is_possible(cubes, maximum_cubes):
    return (
        ("red" not in cubes or cubes["red"] <= maximum_cubes["red"])
        and ("green" not in cubes or cubes["green"] <= maximum_cubes["green"])
        and ("blue" not in cubes or cubes["blue"] <= maximum_cubes["blue"])
    )

if __name__ == '__main__':
    with open("puzzle_input.txt", "r") as file:
        games_raw = file.read().split("\n")

    parsed_games = [parse_game_data(game_raw) for game_raw in games_raw]

    print(parsed_games[0])

    maximum_cubes = {"red": 12, "green": 13, "blue": 14}

    total = 0

    for id, game_info in parsed_games:
        combination_is_possible = True
        for cubes in game_info:
            if not is_possible(cubes, maximum_cubes):
                combination_is_possible = False
                break
        if combination_is_possible:
            total += id

    print(total)
