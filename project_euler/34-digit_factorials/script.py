import math

good_numbers = []

for num in range(1, 10000000):
    if sum(math.factorial(int(str(num)[i])) for i in range(len(str(num)))) == num:
        good_numbers.append(num)


print(good_numbers)