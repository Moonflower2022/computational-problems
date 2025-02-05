import sys

with open(sys.argv[1], "r") as input_file:
    lines = input_file.read().split("\n")

def differences_are_safe(differences):
    if not (all([difference > 0 for difference in differences]) or all([difference < 0 for difference in differences])):
        return False
    if not all([1 <= abs(difference) <= 3 for difference in differences]):
        return False
    return True

def get_differences(numbers):
    differences = []

    for i in range(len(numbers)):
        if i != len(numbers) - 1:
            differences.append(numbers[i] - numbers[i + 1])

    return differences


def get_numbers_with_damping(numbers):
    differences_with_damping = [numbers]

    for i in range(len(numbers)):
        copy = numbers[:]
        copy.pop(i)

        differences_with_damping.append(copy)

    return differences_with_damping

num_safe_reports = 0

for line in lines:
    original_numbers = [int(str_num) for str_num in line.split(" ")]

    increasing = None

    numbers_with_damping = get_numbers_with_damping(original_numbers)

    for numbers in numbers_with_damping:
        if differences_are_safe(get_differences(numbers)):
            num_safe_reports += 1
            break

print(num_safe_reports)