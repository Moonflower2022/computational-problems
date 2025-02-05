import os
from collections import defaultdict

script_dir = os.path.dirname(
    os.path.abspath(__file__)
)  # get the directory of the current script
file_path = os.path.join(script_dir, "puzzle_input.txt")

with open(file_path, "r") as input_file:
    string = input_file.read()


def get_index_of_contiguous_space(disk_representation, length):
    for i in range(len(disk_representation) - length + 1):
        if all(char == "." for char in disk_representation[i : i + length]):
            return i
    return -1


def get_check_sum(array):
    return sum(
        [i * int(element) if element != "." else 0 for i, element in enumerate(array)]
    )


def list_to_string(list_representation):
    disk_string = ""

    for pair in list_representation:
        if pair[1] != ".":
            disk_string += str(pair[1]) * pair[0]
        else:
            disk_string += "." * pair[0]

    return disk_string


disk_representation = []
file_lengths = defaultdict(str)

is_file = True
index = 0
for char in string:
    if is_file:
        disk_representation += [str(index)] * int(char)
        file_lengths[str(index)] = int(char)
        index += 1
    else:
        disk_representation += ["."] * int(char)
    is_file = not is_file

print(disk_representation)

for file_index in list(file_lengths.keys())[::-1]:
    index_of_contiguous_space = get_index_of_contiguous_space(
        disk_representation, file_lengths[file_index]
    )
    if index_of_contiguous_space != -1:
        starting_index = disk_representation.index(file_index)

        if starting_index < index_of_contiguous_space:
            continue
        (
            disk_representation[
                starting_index : starting_index + file_lengths[file_index]
            ],
            disk_representation[
                index_of_contiguous_space : index_of_contiguous_space
                + file_lengths[file_index]
            ],
        ) = (
            disk_representation[
                index_of_contiguous_space : index_of_contiguous_space
                + file_lengths[file_index]
            ],
            disk_representation[
                starting_index : starting_index + file_lengths[file_index]
            ],
        )

print(get_check_sum(disk_representation))
