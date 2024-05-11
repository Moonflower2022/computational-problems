import math

#def y(x, d):
#    return math.sqrt((x ** 2 - 1) / d)

def x(y, d):
    return math.sqrt(1 + d * y ** 2)

def is_int(num):
    return num == int(num)

max_d = 0
max_x = 0
for d in range(1, 1000):
    print(f"d: {d}/1000", end="\r")
    if not math.sqrt(d) - math.isqrt(d) == 0:
        y = 1
        while not is_int(x(y, d)) or x(y, d) == 0:
            y += 1

        if x(y, d) > max_x:
            max_d = d
            max_x = x(y, d)
print(max_d)