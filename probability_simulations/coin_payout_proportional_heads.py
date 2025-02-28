import random

def arithmetic_mean_threshold(num_heads, num_flips):
    return num_heads / num_flips > 0.55

def geometric_mean_threshold(num_heads, num_flips):
    return (((num_heads * (num_heads + 1)) ** (1/2)) / (num_flips + 1)) > (num_heads / num_flips)

def simulate():
    num_heads = random.randint(0, 1)
    num_flips = 1

    i = 0
    while not arithmetic_mean_threshold(num_heads, num_flips):
        if random.random() < 0.5:
            num_heads += 1
        num_flips += 1
        i += 1
        if i > 10000:
            break

    return num_heads / num_flips, i

if __name__ == "__main__":
    iterations = 100000

    results = [simulate() for _ in range(iterations)]

    print("average ratio:", sum([result[0] for result in results]) / iterations)
    # it should be at least 0.75:
    # first flip
    # H: get proportion of 1
    # T: flip until proportion gets back up to 0.5
    # average is 0.75
    print("average steps:", sum([result[1] for result in results]) / iterations)