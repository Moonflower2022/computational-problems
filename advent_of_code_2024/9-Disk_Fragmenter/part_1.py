def empty_removed(array):
    return [element for element in array if element != "."]

def get_check_sum(array):
    relevant_array = empty_removed(array)
    return sum([i * int(element) for i, element in enumerate(relevant_array)])

def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

def get_index_of_last_non_empty(array):
    i = len(array) - 1
    while array[i] == ".":
        i -= 1
    return i

with open("puzzle_input.txt", "r") as input_file:
    string = input_file.read()

disk_representation = []

is_file = True
index = 0
for char in string:
    if is_file:
        disk_representation += [str(index)] * int(char)
        index += 1
    else:
        disk_representation += ["."] * int(char)
    is_file = not is_file

print(f"length of disk_representation: {len(disk_representation)}")
num_non_empty = len(disk_representation) - disk_representation.count(".")
print(f"count of non empty: {num_non_empty}")

i = 0
while not all([element == "." for element in disk_representation[i:]]):
    print(f"{i}/{num_non_empty}", end="\r")
    if disk_representation[i] == ".":
        swap(disk_representation, i, get_index_of_last_non_empty(disk_representation))
    i += 1
print(i)

print(get_check_sum(disk_representation))