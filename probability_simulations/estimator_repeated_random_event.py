import random
import math

def get_num_events_for_repeat(n):
    seen_events = []
    event = random.randint(1, n)
    while not event in seen_events:
        seen_events.append(event)
        event = random.randint(1, n)
    return len(seen_events) + 1

if __name__ == "__main__":
    n = 263

    iterations = 1000000
    total_num_events_for_repeat = 0
    for _ in range(iterations):
        total_num_events_for_repeat += get_num_events_for_repeat(n)

    print(total_num_events_for_repeat / iterations)
    print(sum([math.factorial(n) * (k - 1) / (n ** k * math.factorial(n - k + 1)) for k in range(1, n + 1)]))
    print(sum([k * math.factorial(n) * (k - 1) / (n ** k * math.factorial(n - k + 1)) for k in range(1, n + 1)]))