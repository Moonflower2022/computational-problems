import math

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

input_num = 600851475143
largest_prime_factor = 0

while input_num != 1:
    for i in range(1, input_num + 1):
        if input_num % i == 0 and is_prime(i):
            input_num = int(input_num / i)
            if i > largest_prime_factor:
                largest_prime_factor = i
            break

print(largest_prime_factor)