good_numbers = []

for num in range(1, 10000000):
    if sum(int(str(num)[i]) ** 5 for i in range(len(str(num)))) == num:
        good_numbers.append(num)

print(good_numbers)