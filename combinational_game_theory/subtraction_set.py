# given a subtraction set and a max index to go up to, 
# the program assigns to and from positions to each index up to the max

# False is F, True is T

start = 1441
# range: start -> 0

# subtraction set [1, 3, 4], to positions are 0 mod 7 and 2 mod 7
# subtraction set [2, 3, 5, 7], to positions are 0 mod 9 and 1 mod 9


subtraction_set = [2, 3, 5, 7]

table = [0] * (start + 1)
table[0] = True

def count_zero(arr):
    count = 0
    for ele in arr:
        if ele is 0:
            count += 1
    return count

def check_for_T(index, table, subtraction_set):
    parity_arr = [not table[index - offset] if index - offset >= 0 else None for offset in subtraction_set]
    return all(parity == True or parity == None for parity in parity_arr)


def fill_F(table, subtraction_set):
    for i in range(len(table)):
        if table[i] == True:
            for offset in subtraction_set:
                if offset + i < len(table):
                    table[offset + i] = False
    return table

def fill_T(table, subtraction_set):
    for i in range(len(table)):
        if check_for_T(i, table, subtraction_set):
            table[i] = True
    return table

while count_zero(table) > 0:
    fill_F(table, subtraction_set)
    fill_T(table, subtraction_set)

print(table)

f_indexes = []

for i in range(len(table)):
    if table[i] == False:
        f_indexes.append(i)

print(f_indexes)

t_indexes = []

for i in range(len(table)):
    if table[i] == True: 
        t_indexes.append(i)

print(t_indexes)