import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def probability_of_heads(alpha, heads_prop):
    if heads_prop == 0:
        return 0
    if heads_prop == 1:
        return 1
    if alpha == 0:
        return 1/2
    return 1/2 + 1/np.pi * np.arctan(alpha * np.pi * (heads_prop - 1/2) / (1 - (2*heads_prop - 1)**2))

def history(iterations, wealth, strategies, alpha):
    wealth_history = []
    for _ in range(iterations):
        wealth_history.append(np.array(wealth.copy()))
        total = sum(wealth)
        heads_prop = wealth.dot(strategies)/total

        is_heads = np.random.rand() < probability_of_heads(alpha, np.round(heads_prop, 5))
        
        if is_heads:
            out_wealth = total * np.multiply(strategies, wealth)/(strategies.dot(wealth))
        else:
            out_wealth = total * np.multiply(np.ones(len(strategies))-strategies, wealth)/(total-(strategies.dot(wealth)))
        wealth = out_wealth
    return wealth_history

def history_with_rational(iterations, wealth, strategies, alpha):
    player_num = len(wealth)
    wealth_history = []
    for _ in range(iterations):

        strategies = np.append(strategies, rational_strat(wealth, strategies, alpha, wealth[player_num-1], player_num))
        
        wealth_history.append(np.array(wealth.copy()))
        total = sum(wealth)
        heads_prop = wealth.dot(strategies) / total

        is_heads = np.random.rand() < probability_of_heads(alpha, np.round(heads_prop, 5))
        
        if is_heads:
            out_wealth = total * np.multiply(strategies, wealth)/(strategies.dot(wealth))
        else:
            out_wealth = total * np.multiply(np.ones(len(strategies))-strategies, wealth)/(total-(strategies.dot(wealth)))
        wealth = out_wealth
        strategies = np.delete(strategies, player_num - 1)
    return wealth_history

def one_on_one_result(iterations, wealth, strategies, alpha, prop_wealth):
    for _ in range(iterations):
        total = sum(wealth)
        heads_prop = wealth.dot(strategies) / sum(wealth)

        is_heads = np.random.rand() < probability_of_heads(alpha, np.round(heads_prop, 5))

        if is_heads:
            wealth = np.round(total * np.multiply(strategies, wealth)/(strategies.dot(wealth)), 5)
        else:
            wealth = np.round(total * np.multiply(np.ones(len(strategies))-strategies, wealth)/(total-(strategies.dot(wealth))), 5)
    if prop_wealth:
        return wealth[0] / sum(wealth)
    return 0.5 if wealth[1] == wealth[0] else 1 if wealth[0] > wealth[1] else 0
    
def individual_gain(wealth, strategies, alpha, our_strat, our_wealth, is_heads):
    total_wealth = np.append(wealth, our_wealth)
    total_strategies = np.append(strategies, our_strat)
    if is_heads:
        return sum(total_wealth) * our_strat * our_wealth / total_wealth.dot(total_strategies)
    else: 
        return sum(total_wealth) * (1 - our_strat) * our_wealth / total_wealth.dot(1 - total_strategies)

def expected_value(our_strat, args):
    wealth, strategies, alpha, our_wealth = args
    total_wealth = np.append(wealth, our_wealth)
    total_strategies = np.append(strategies, our_strat)
    heads_proportion = total_wealth.dot(total_strategies) / sum(total_wealth)
    heads_prob = probability_of_heads(alpha, np.round(heads_proportion, 5))
    return -(
        heads_prob * individual_gain(wealth, strategies, alpha, our_strat, our_wealth, True) +
        (1 - heads_prob) * individual_gain(wealth, strategies, alpha, our_strat, our_wealth, False)
            )

def rational_strat(wealth, strategies, alpha, our_wealth, player_num):
    initial_guess = 0.0
    parameter_bounds = [(0, 1)]
    result = minimize(
        expected_value, 
        initial_guess, 
        args=((np.delete(wealth, player_num - 1), strategies, alpha, our_wealth),), 
        bounds=parameter_bounds
    )
    return result.x

'''
# one sim with stationary dudes
iterations = 21

strategies = np.round(np.arange(0, 1.1, 0.1), 2)

player_num = len(strategies)

wealth_per_player = 100

wealth = np.array([100 for i in range(player_num)], dtype=float)

alpha = 1

fig, ax = plt.subplots()

data = np.array(history(iterations, wealth, strategies, alpha)).T

for i in range(player_num):
  ax.plot(data[i], label=f"{strategies[i]}")

leg = plt.legend(loc='upper left')

plt.show()
'''

'''
# the matrix color grid between stationary strategies
from mpl_toolkits.axes_grid1 import make_axes_locatable

prop_wealth = False

iterations_per_game = 20
iterations_per_match = 500

alpha = 0

game_results = np.zeros((21, 21), dtype=float)

for i in range(21):
    for j in range(21):
        strategies = np.array([i * 0.05, j * 0.05], dtype=float)
        wealth = np.array([200, 200], dtype=float)
        game_results[i][j] = sum([one_on_one_result(iterations_per_game, wealth, strategies, alpha, prop_wealth) for i in range(iterations_per_match)]) / iterations_per_match

fig, ax = plt.subplots()

im = ax.imshow(game_results, cmap='jet', vmin=0, vmax=1)


ax = plt.gca()
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')

custom_xticks = np.arange(0, 21)
custom_yticks = np.arange(0, 21)

plt.xticks(custom_yticks, labels=np.round(np.arange(0, 1.05, 0.05, dtype=float), 2))
plt.yticks(custom_yticks, labels=np.round(np.arange(0, 1.05, 0.05, dtype=float), 2))

plt.xticks(rotation=90)

plt.xlabel('Player 2')
plt.ylabel('Player 1')

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

custom_ticks = np.arange(0, 1.1, 0.1)
plt.colorbar(im, cax=cax, ticks=custom_ticks)

plt.title(f"{iterations_per_game} rounds per sim, {iterations_per_match} simulations, alpha = {alpha} \n " + ("proportion of wealth held by player 1" if prop_wealth else "proportion of simulations won by player 1"), loc='center', x = -10, y = 1.2)

plt.show()
'''

'''
# one sim of a rational player and a buncha other stationary strategies
alpha = 2

iterations = 21

strategies = np.round(np.arange(0.1, 1, 0.1), 2)

player_num = len(strategies) + 1 # for rational player

wealth_per_player = 100

wealth = np.array([100 for i in range(player_num)], dtype=float)

fig, ax = plt.subplots()

data = np.array(history_with_rational(iterations, wealth, strategies, alpha)).T

for i in range(player_num):
  if i == player_num - 1:
      ax.plot(data[i], label="Rational Player")
      break
  ax.plot(data[i], label=f"{strategies[i]}")

leg = plt.legend(loc='upper left')

plt.show()
'''

# running x sims with specific opponents and find what percent the rational player wins
alpha = 0.5

iterations = 21

sims = 1000

wins = 0
percentages = 0

strategies = np.array([0, 0.1, 0.2, 0.3, 0.4])
#np.arange(0, 1.1, 0.1)
#
player_num = len(strategies) + 1 # for rational player
wealth_per_player = 100
wealth = np.array([100 for _ in range(player_num)], dtype=float)

for _ in range(sims):
    data = np.array(history_with_rational(iterations, wealth, strategies, alpha))
    if np.argmax(data[iterations - 1]) == player_num - 1:
        wins += 1
    percentages += data[iterations - 1][player_num - 1] / sum(data[iterations - 1])
    
print("simulations: ", sims)
print("iterations per sim: ", iterations)
print("alpha: ", alpha)
print("other strategies: ", strategies)
print("rational player win percent: ", wins/sims)
print("rational player average wealth percentage: ", percentages/sims)
print("percentage of population: ", 1/player_num)

'''
# running x sims with n random stationary players and find what percent the rational player wins
alpha = 1

games = 20

iterations = 21

sims = 1000

player_num = 12

wealth_per_player = 100

wins_arr = []
percentages_arr = []

for __ in range(games):
    wins = 0
    percentages = 0

    wealth = np.array([100 for _ in range(player_num)], dtype=float)
    for _ in range(sims):
        strategies = np.random.rand(player_num - 1)
        data = np.array(history_with_rational(iterations, wealth, strategies, alpha))
        if np.argmax(data[iterations - 1]) == player_num - 1:
            wins += 1
        percentages += data[iterations - 1][player_num - 1] / sum(data[iterations - 1])
    wins_arr.append(wins)
    percentages_arr.append(percentages)

fig, (ax1, ax2) = plt.subplots(2, 1)

data1 = np.array(player_num*np.array(wins_arr)/sims)
data2 = np.array(player_num*np.array(percentages_arr)/sims)

ax1.plot(data1)
ax1.set_ylabel("Wins")

ax2.plot(data2)
ax2.set_ylabel("% Wealth")

plt.xticks(np.arange(0, games, 1))

plt.show()
'''