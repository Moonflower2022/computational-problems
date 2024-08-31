# We will consider a new dynamical model for a firm’s market share. Let M_n ∈ [0, 1]
# denote the market share at time n and let
# Mn+1 = 1 / (1 + α / (β ^ (M_n)))

# describe the evolution of the market share, where 4 ≤ α ≤ 10 and 60 ≤ β ≤ 100
# are two parameters.

import numpy as np
import matplotlib.pyplot as plt
import math

def within_x_percent(number1, number2, x):
    return abs(number1 - number2) / number2 <= x / 100

def iterate(market_share, a, b):
    return 1 / (1 + a / (math.pow(b, market_share)))

def history(market_share, a, b, iterations):
    market_share_history = []
    for _ in range(iterations):
        market_share_history.append(market_share)
        market_share = iterate(market_share, a, b)
    return market_share_history

def rounds_to_stablize(market_share, a, b, iterations):
    market_share_history = []
    for _ in range(iterations):
        market_share_history.append(market_share)
        market_share = iterate(market_share, a, b)

    rounds = 0
    for i in range(iterations):
        if within_x_percent(market_share_history[-1], market_share_history[i], 1):
            break
        else: 
            rounds += 1
    return rounds


'''
a = 7
b = 100

market_share = 0.5

iterations = 30

print(rounds_to_stablize(market_share, a, b, iterations))

fig, ax = plt.subplots()

ax.plot(np.array(history(market_share, a, b, iterations)))

plt.show()
'''

market_share = 0.5

iterations = 30

rounds_matrix = np.zeros((61, 61))

for a in range(61):
    for b in range(61):
        a_1 = (a + 40) / 10
        b_1 = b * 2/3 + 60
        rounds_matrix[a][b] = rounds_to_stablize(market_share, a_1, b_1, iterations)

fig, ax = plt.subplots()

im = ax.imshow(rounds_matrix, cmap='jet')

ax = plt.gca()
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')

'''
custom_xticks = np.arange(0, 7)
custom_yticks = np.arange(0, 41)

plt.xticks(custom_xticks, labels=np.round(np.arange(4, 11, 1, dtype=float), 2))
plt.yticks(custom_yticks, labels=np.round(np.arange(60, 101, 1, dtype=float), 2))
'''

plt.xticks(rotation=90)

plt.xlabel('beta')
plt.ylabel('alpha')


plt.show()
