def get_xmas_count(puzzle, targets):
    xmas_count = 0

    for i in range(1, len(puzzle) - 1):
        for j in range(1, len(puzzle[i]) - 1):
            if get_diagonal((i, j), puzzle) in targets and get_other_diagonal((i, j), puzzle) in targets:
                xmas_count += 1

    return xmas_count

def get_other_diagonal(indices, puzzle):
    x, y = indices
    return [puzzle[x - i][y + i] for i in [-1, 0, 1]]

def get_diagonal(indices, puzzle):
    x, y = indices
    return [puzzle[x + i][y + i] for i in [-1, 0, 1]]

with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

puzzle = [list(line) for line in lines]

targets = (["M", "A", "S"], ["S", "A", "M"])

print(get_xmas_count(puzzle, targets))