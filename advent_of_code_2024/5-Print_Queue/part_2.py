def get_middle_element(array):
    assert len(array) % 2 == 1

    return array[len(array) // 2]


def update_complies_by_rules(update, rules):
    for rule in rules:
        if (
            rule[0] in update
            and rule[1] in update
            and not update.index(rule[0]) < update.index(rule[1])
        ):
            return False
    return True


def get_fixed_update(update, rules):
    new_update = update[:]
    for rule in rules:
        if (
            rule[0] in new_update
            and rule[1] in new_update
            and not new_update.index(rule[0]) < new_update.index(rule[1])
        ):
            (
                new_update[new_update.index(rule[0])],
                new_update[new_update.index(rule[1])],
            ) = (rule[1], rule[0])
    return new_update


with open("puzzle_input.txt", "r") as input_file:
    lines = input_file.read().split("\n")

split_index = lines.index("")

ordering_rules = [line.split("|") for line in lines[:split_index]]
updates = [line.split(",") for line in lines[split_index + 1 :]]

print(ordering_rules)
print(updates)

middle_element_total = 0

for update in updates:
    if not update_complies_by_rules(update, ordering_rules):
        fixed_update = get_fixed_update(
            get_fixed_update(
                get_fixed_update(
                    get_fixed_update(update, ordering_rules), ordering_rules
                ),
                ordering_rules,
            ),
            ordering_rules,
        )
        # ↑ lmao
        print(update_complies_by_rules(fixed_update, ordering_rules))
        middle_element_total += int(get_middle_element(fixed_update))

print(middle_element_total)
