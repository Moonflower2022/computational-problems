import random
import math
import matplotlib.pyplot as plt

gamma = 1
bids = list(range(1, 101))
value = 100

def distribution(x):
    return -math.log(x)/gamma # this is my way of sampling from my distribution

simulations = 1000

profit_averages = [sum((bid > distribution(random.random())) * (value - bid) for _ in range(simulations))/simulations for bid in bids]

print(profit_averages)

plt.plot(profit_averages)
plt.title(f"Bidding Simulation for gamma = {gamma}")
plt.xlabel("Bid Amount")
plt.ylabel("Average Profit")
plt.show()