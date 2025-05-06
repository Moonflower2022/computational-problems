import random

def generate_radius():
    while True:
        x, y = random.random(), random.random()
        if (x ** 2 + y ** 2) <= 1:
            break
    return (x ** 2 + y ** 2) ** (1/2)

def sample_radius():
    return (random.random()) ** (1/2)

if __name__ == "__main__":
    iterations = 10_000_000

    print("generation avg:", sum([generate_radius() for _ in range(iterations)])/iterations)
    print("sample avg:", sum([sample_radius() for _ in range(iterations)])/iterations)

# output:
# generation avg: 0.6666898508697755
# sample avg: 0.6666400049942893