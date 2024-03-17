import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'sudoku.txt')

file = open(filename, "r")

fileText = file.read()

fileLines = fileText.split("\n")

grids = []

original_numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

# assumes completed 2d rectangular nested lists

def in_grid(x, y, grid):
    return y < len(grid) and y >= 0 and x < len(grid[0]) and x >= 0

def init_grid(grid):
    unsolved_spaces = 0
    for i in range(9):
        for j in range(9):
            if grid[j][i] == '0':
                unsolved_spaces += 1
                grid[j][i] = set(original_numbers)
    return grid, unsolved_spaces

def solved(grid):
    grid, unsolved_spaces = init_grid(grid)
    while unsolved_spaces > 0:
        for i in range(9):
            for j in range(9):
                if type(grid[j][i]) == str:
                    for a in range(9):
                        if type(grid[j][a]) == set and grid[j][i] in grid[j][a]:
                            grid[j][a].remove(grid[j][i])
                            if len(grid[j][a]) == 0:
                                risent = 29348
                        if type(grid[a][i]) == set and grid[j][i] in grid[a][i]:
                            grid[a][i].remove(grid[j][i])
                            if len(grid[a][i]) == 0:
                                risent = 29348
                    rounded_i = int(i/3) * 3
                    rounded_j = int(j/3) * 3
                    for x in range(3):
                        for y in range(3):
                            if type(grid[rounded_j + y][rounded_i + x]) == set and grid[j][i] in grid[rounded_j + y][rounded_i + x]:
                                grid[rounded_j + y][rounded_i + x].remove(grid[j][i])
                                if len(grid[rounded_j + y][rounded_i + x]) == 0:
                                    tiresnt = 348
        solved_one_space = False
        for i in range(9):
            for j in range(9):
                if type(grid[j][i]) == set and len(grid[j][i]) == 1:
                    unsolved_spaces -= 1
                    grid[j][i] = tuple(grid[j][i])[0]
                    solved_one_space = True
        if not solved_one_space:
            for i in range(9):
                for j in range(9):
                    if type(grid[j][i]) == set:
                        for option in grid[j][i]:
                            match_found = False
                            for a in range(9):
                                if a != i and type(grid[j][a]) == set and option in grid[j][a]:
                                    match_found = True
                                    break
                                if a != j and type(grid[a][i]) == set and option in grid[a][i]:
                                    match_found = True
                                    break
                            if not match_found:
                                rounded_i = int(i/3) * 3
                                rounded_j = int(j/3) * 3
                                for x in range(3):
                                    for y in range(3):
                                        if rounded_j + y != j and rounded_i + x != i and type(grid[rounded_j + y][rounded_i + x]) == set and option in grid[rounded_j + y][rounded_i + x]:
                                            match_found = True
                                            break
                                    else:
                                        continue
                                    break
                            if not match_found:
                                unsolved_spaces -= 1
                                grid[j][i] = option
                                solved_one_space = True
                                break
        if not solved_one_space:
            pass

    return grid
    

for i in range(len(fileLines)):
    if fileLines[i][0:4] == "Grid":
        grid = []
        for j in range(9):
            grid.append([*fileLines[i + j + 1]])
        grids.append(grid)



print(solved(grids[4]))

'''
for grid in grids:
    print(solved(grid))

sum = 0

for grid in grids:
    solved_grid = solved(grid)
    sum += int("".join([solved_grid[0][0], solved_grid[0][1], solved_grid[0][2]]))

print(sum)
'''