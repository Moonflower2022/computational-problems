def get_index(string, sub_string):
    try:
        return string.index(sub_string)
    except:
        return 100

def get_calibration_number(string):
    number_string_map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    
    indices = [(get_index(string, number_string), number_string_map[number_string]) for number_string in number_string_map.keys()]

    sorted_indices = sorted(indices, key=lambda pair: pair[0])

    backward_indices = [(get_index(string[::-1], number_string[::-1]), number_string_map[number_string]) for number_string in number_string_map.keys()]

    backward_sorted_indices = sorted(backward_indices, key=lambda pair: pair[0])

    return 10 * sorted_indices[0][1] + backward_sorted_indices[0][1]

if __name__ == "__main__":
    with open("puzzle_input.txt", "r") as file:
        puzzle_input = file.read().split("\n")

    print(puzzle_input)

    print(sum(get_calibration_number(string) for string in puzzle_input))
