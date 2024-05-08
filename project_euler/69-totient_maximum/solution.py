import time

def phi(n):
    result = n
    i = 2
    while i ** 2 < n:
        if n % i == 0:            
            while n % i == 0:
                n /= i    
            result -= result / i
        i += 1
    if n > 1:
        result -= result / n
    return result

biggest = 0
index = None

start_time = time.time()

for i in range(10, 1_000_001):
    print(f"{biggest}: {index}, {i}", end="\r")
    if i / phi(i) > biggest:
        biggest = i / phi(i)
        index = i

print("Running time (s):", time.time() - start_time)

print("Biggest:", biggest)
print("Index:", index)