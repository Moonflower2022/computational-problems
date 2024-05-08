import time
import random
import numpy as np
import multiprocessing as mp
from functools import partial

def avg(arr):
    return sum(arr) / len(arr)

class MultiArmedBandit:
    def __init__(self, arms, max_steps, seed=None):
        self.arms = arms
        if seed:
            random.seed(seed)
        self.probabilities = [random.random() for _ in range(arms)]
        self.histories = [[] for _ in range(arms)]
        self.steps = 0
        self.max_steps = max_steps

    def pull(self, arm_index, seed=None):
        self.steps += 1
        if seed:
            random.seed(seed)
        if random.random() < self.probabilities[arm_index]:
            result = 1
        else:
            result = 0
        
        self.histories[arm_index].append(result)

    def score(self):
        return sum(sum(history) for history in self.histories)

def random_arm(mab):
    return random.randint(0, mab.arms - 1)

def best_arm(mab):
    ratios = [avg(history) if len(history) > 0 else 0 for history in mab.histories]
    return np.argmax(ratios)

def epsilon_greedy(mab, epsilon=0.2):
    if random.random() < epsilon:
        mab.pull(random_arm(mab))
    else:
        mab.pull(best_arm(mab))

def epsilon_first(mab, epsilon=0.2):
    if mab.steps / mab.max_steps < epsilon:
        mab.pull(random_arm(mab))
    else:
        mab.pull(best_arm(mab))

def epsilon_decreasing(mab):
    if random.random() < mab.steps / mab.max_steps:
        mab.pull(best_arm(mab))
    else:
        mab.pull(random_arm(mab))

def simulate(i, strategy=lambda x: x, arms=4, max_steps=100):
    mab = MultiArmedBandit(arms, max_steps)

    for _ in range(max_steps):
        strategy(mab)

    return mab.score()

def simulate_epsilon_range(strategy, simulations, arms, max_steps):
    print("Espilon Average")
    with open("output.txt", "w") as file:
        for i in range(1, 20):
            print(f"{i - 1}/20", end="\r")

            strategy_partial = partial(strategy, epsilon=i/20)

            simulate_partial = partial(simulate, strategy=strategy_partial, arms=arms, max_steps=max_steps)

            with mp.Pool(mp.cpu_count()) as pool:
                total = sum(pool.map(simulate_partial, list(range(simulations))))

            print(f"{i/20} {total / simulations}")
        
            file.write(f'{i/20}\t{total / simulations}\n')

def simulate_normal(strategy, simulations, arms, max_steps):
    simulate_partial = partial(simulate, strategy=strategy, arms=arms, max_steps=max_steps)

    with mp.Pool(mp.cpu_count()) as pool:
        total = sum(pool.map(simulate_partial, list(range(simulations))))

    print(f"Average: {total /  simulations}")

if __name__ == '__main__':
    SIMULATIONS = 100000

    ARMS = 10
    MAX_STEPS = 200

    strategy = epsilon_first

    print("Simulations:", SIMULATIONS)
    print("Arms:", ARMS)
    print("Max Steps:", MAX_STEPS)
    print("Strategy:", strategy.__name__)
    start_time = time.time()
    simulate_epsilon_range(strategy, SIMULATIONS, ARMS, MAX_STEPS)
    print("Running Time (s):", time.time() - start_time)
