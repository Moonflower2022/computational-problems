a = 0
b = 1
i = 0
total = 0

while True:
    if i % 2 == 0:
        a = a + b
        if a >= 4_000_000:
            break
        if a % 2 == 0:
            total += a
    else:
        b = a + b
        if b >= 4_000_000:
            break
        if b % 2 == 0:
            total += b
    i += 1

print(total)