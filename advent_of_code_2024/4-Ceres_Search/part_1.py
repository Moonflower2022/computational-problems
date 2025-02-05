def get_horizontal_count(puzzle, targets):
    horizontal_count = 0

    for row in puzzle:
        for j in range(len(row)):
            if row[j : j + 4] in targets:
                horizontal_count += 1

    return horizontal_count


def get_diagonal_count(puzzle, targets):
    diagonal_count = 0

    for i, row in enumerate(puzzle):
        for j in range(len(row)):
            if get_diagonal((i, j), puzzle) in targets:
                diagonal_count += 1

    return diagonal_count


def get_diagonal(indices, puzzle, length=4):
    x, y = indices
    return [puzzle[x + i][y + i] for i in range(length) if x + i < len(puzzle) and y + i < len(puzzle[x+i])]


def get_transpose(matrix):
    transpose = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i, row in enumerate(matrix):
        for j in range(len(row)):
            transpose[j][i] = matrix[i][j]
    return transpose

def reflect(matrix):
    return [row[::-1] for row in matrix]


with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

puzzle = [list(line) for line in lines]

targets = (["X", "M", "A", "S"], ["S", "A", "M", "X"])

total_count = (
    get_horizontal_count(puzzle, targets)
    + get_horizontal_count(get_transpose(puzzle), targets)
    + get_diagonal_count(puzzle, targets)
    + get_diagonal_count(reflect(puzzle), targets)
)

print(total_count)