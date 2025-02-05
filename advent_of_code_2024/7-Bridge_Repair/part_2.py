from itertools import product

def parse_line(line):
    test_value_string, number_strings = line.split(": ")
    return [int(test_value_string), [int(number_string) for number_string in number_strings.split(" ")]]

def can_produce(equation):
    test_value, numbers = equation
    options = product(["*", "+", "|"], repeat=len(numbers) - 1)

    for option in options:
        current_total = numbers[0]
        for i in range(1, len(numbers)):
            if option[i - 1] == "*":
                current_total *= numbers[i]
            elif option[i - 1] == "+":
                current_total += numbers[i]
            elif option[i - 1] == "|":
                current_total = int(str(current_total) + str(numbers[i]))
        if current_total == test_value:
            return True
    return False
        

with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

equations = [parse_line(line) for line in lines]

total_test_value = 0

for equation in equations:
    if can_produce(equation):
        total_test_value += equation[0]

print(total_test_value)