with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

def report_is_safe(differences):
    if not (all([difference > 0 for difference in differences]) or all([difference < 0 for difference in differences])):
        return False
    if not all([1 <= abs(difference) <= 3 for difference in differences]):
        return False
    return True

num_safe_reports = 0

for line in lines:
    numbers = [int(str_num) for str_num in line.split(" ")]

    increasing = None

    differences = []

    for i in range(len(numbers)):
        if i != len(numbers) - 1:
            differences.append(numbers[i] - numbers[i + 1])
    
    if report_is_safe(differences):
        num_safe_reports += 1

print(num_safe_reports)