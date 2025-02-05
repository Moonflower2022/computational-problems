import random

classes = [i for _ in range(6) for i in range(5)]

print(classes)

iterations = 1000000
good = 0

good_set = {0, 1, 2, 3, 4}

for i in range(iterations):
    if set(random.sample(classes, 7)) == good_set:
        good += 1

print(good/iterations)