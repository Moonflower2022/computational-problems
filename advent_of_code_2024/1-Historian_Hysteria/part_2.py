with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

pairs = [line.split("   ") for line in lines]

list1 = []
list2 = []

for num1, num2 in pairs:
    list1.append(int(num1))
    list2.append(int(num2))

total_similarity = 0

for num1 in list1:
    total_similarity += num1 * list2.count(num1)

print(total_similarity)