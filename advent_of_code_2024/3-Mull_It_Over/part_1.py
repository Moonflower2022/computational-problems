import sys

def parse_arguments(arguments):
    argument_strings = arguments.split(",")
    if len(argument_strings) != 2:
        return 0
    for argument_string in argument_strings:
        if argument_string != argument_string.strip():
            return 0
        if not argument_string.isnumeric():
            return 0
    return int(argument_strings[0]) * int(argument_strings[1])
    
        
    

def get_next_close_parentheses_index(line, i):
    for j in range(i+1, len(line)):
        if line[j] == ")":
            return j
    return -1

def parse_line(line):
    total = 0
    for i in range(len(line)):
        if line[i:i+4] == "mul(":
            next_close_parentheses_index = get_next_close_parentheses_index(line, i)
            if next_close_parentheses_index == -1:
                break
            arguments = line[i+4:next_close_parentheses_index]

            total += parse_arguments(arguments)

    return total

with open(sys.argv[1], "r") as input_file:
    lines = input_file.read().split("\n")

    print(sum([parse_line(line) for line in lines]))

