final = 0
fib_1 = 1
fib_2 = 2
fib_3 = 3
while fib_1 < 4000000:
    fib_1 = fib_2
    fib_2 = fib_3
    fib_3 = fib_2 + fib_1

    if fib_1 % 2 == 0:
        final = final + fib_1
print(final)
