def get_middle_element(array):
    assert len(array) % 2 == 1

    return array[len(array) // 2]

def update_complies_by_rules(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update and not update.index(rule[0]) < update.index(rule[1]):
            return False
    return True

with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

split_index = lines.index("")

ordering_rules = [line.split("|") for line in lines[:split_index]]
updates = [line.split(",") for line in lines[split_index + 1:]]

print(ordering_rules)
print(updates)

middle_element_total = 0

for update in updates:
    if update_complies_by_rules(update, ordering_rules):
        middle_element_total += int(get_middle_element(update))

print(middle_element_total)