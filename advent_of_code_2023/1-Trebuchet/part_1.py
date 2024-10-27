
def get_calibration_number(string):
    digits = []
    for char in string:
        if char.isdigit():
            digits.append(int(char))
    return 10 * digits[0] + digits[-1]

if __name__ == '__main__':
    with open("puzzle_input.txt", "r") as file:
        puzzle_input = file.read().split("\n")

    print(puzzle_input)

    print(sum(get_calibration_number(string) for string in puzzle_input))