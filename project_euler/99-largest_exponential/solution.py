import math

with open("0099_base_exp.txt") as file:
    string_pairs = [string.split(",") for string in file.read().split("\n")]
    base_exp_pairs = [(int(pair[0]), int(pair[1])) for pair in string_pairs]

largest_index = None
largest_number = 0

for i, pair in enumerate(base_exp_pairs):
    base, exp = pair
    number = math.log(exp) + math.log(math.log(base)) # b^e -> log(b^e) = e*log(b) -> log(e*log(b)) = log(e) + log(log(b))
    if number > largest_number:
        largest_index = i + 1
        largest_number = number

print(largest_index)