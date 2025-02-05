with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

pairs = [line.split("   ") for line in lines]

list1 = []
list2 = []

for num1, num2 in pairs:
    list1.append(int(num1))
    list2.append(int(num2))

list1.sort()
list2.sort()

total_distance = 0

for sorted_num1, sorted_num2 in zip(list1, list2):
    total_distance += abs(sorted_num1 - sorted_num2)

print(total_distance)