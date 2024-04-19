import time
import sys

if len(sys.argv) != 2:
    raise Exception("This program expects one extra command line argument.")

total = 0
start_time = time.time()

for i in range(1, int(sys.argv[1]) + 1):
    total += i ** i

print("Sum:", total)
print("Running Time (s):", time.time() - start_time)

