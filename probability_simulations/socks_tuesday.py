import random

def simulation(socks, days):
    # this would be much nicer with a Kid class and attributes for socks and days of the week but i just couldnt bother

    kid1 = (random.choice(socks), random.choice(days))
    kid2 = (random.choice(socks), random.choice(days))

    if (kid1[0] == 0 and kid1[1] == 1) or (kid2[0] == 0 and kid2[1] == 1):
        if kid1[0] == 0 and kid2[0] == 0:
            return True
        return False
    return None

if __name__ == "__main__":
    socks = [0, 1] # 0 is blue, 1 is white
    days = list(range(7))

    iterations = 1000000

    total_success = 0
    total_failure = 0
    for _ in range(iterations):
        result = simulation(socks, days)
        if result == True:
            total_success += 1
        elif result == False:
            total_failure += 1
    print(total_success / (total_failure + total_success))