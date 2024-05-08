import random
import math
import matplotlib.pyplot as plt

l = 0.01
n = 3

bids = list(range(1, 101))
value = 100

def distribution(x):
    return -math.log(x)/l # this is my way of sampling from my distribution

simulations = 100000

profit_averages = [sum(all((bid > distribution(random.random())) for _ in range(n)) * (value - bid) for _ in range(simulations))/simulations for bid in bids]

sorted_bids = [bid for _, bid in sorted(zip(profit_averages, bids), reverse=True)]

print("Ranked Bids:", sorted_bids)

plt.plot(profit_averages)
plt.title(f"Bidding Simulation for lambda = {l}, n = {n}")
plt.xlabel("Bid Amount")
plt.ylabel("Average Profit")
plt.show()