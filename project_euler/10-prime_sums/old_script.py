# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
threshold = 2_000_000
sum = 0


def isPrime(num):
    if num < 2:
        return False
    for i in range(num):
        if int(num/(i + 1)) - num/(i + 1) == 0 and not (i + 1 == 1 or i + 1 == num):
            return False
    return True


for i in range(threshold):
    if isPrime(i + 1):
        sum += i + 1
print(sum)
