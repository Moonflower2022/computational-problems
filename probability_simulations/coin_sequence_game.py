import random
from itertools import product
import numpy as np
import matplotlib.pyplot as plt

def get_coin_flip():
    return "H" if random.random() < 0.5 else "T"

def simulate_game(sequence1, sequence2, n=3):
    last_sequence = ""

    for _ in range(n):
        last_sequence += get_coin_flip()

    while sequence1 != last_sequence and sequence2 != last_sequence:
        last_sequence += get_coin_flip()
        last_sequence = last_sequence[1:]

    return 1 if last_sequence == sequence1 else 0


N = 3
iterations = 1000000

coin_sequences = sorted(["".join(sequence) for sequence in product("HT", repeat=N)])

print({i: coin_sequence for i, coin_sequence in enumerate(coin_sequences)})

results = np.zeros((2 ** N, 2 ** N))

for i, coin_sequence1 in enumerate(coin_sequences):
    for j, coin_sequence2 in enumerate(coin_sequences):
        if i == j:
            # continue
            break

        results[i][j] = sum([simulate_game(coin_sequence1, coin_sequence2, n=N) for _ in range(iterations)]) / iterations

print(results)

header = f"{'':10s}"

for sequence in coin_sequences:
    header += f"{sequence:10s}"

print(header)

for i, row in enumerate(results):
    print(f"{coin_sequences[i]:10s}", end="")
    for element in row:
        print(f"{element:<10.2f}", end="")
    print("")

def plot_sequence_heatmap(coin_sequences, results, title="Coin Sequence Results"):
    """
    Create a heatmap of coin sequence results.
    
    Args:
        coin_sequences (list): List of sequence names/identifiers
        results (list): 2D list/array of numerical results
        title (str): Title for the plot
    """
    results_array = np.array(results)
    
    # Create figure and axis with specified size
    plt.figure(figsize=(10, 6))
    
    # Create heatmap
    im = plt.imshow(results_array, cmap='RdYlBu_r')  # Red for high, Blue for low
    
    # Add colorbar
    plt.colorbar(im)
    
    # Add labels
    plt.xticks(np.arange(len(coin_sequences)), coin_sequences)
    plt.yticks(np.arange(len(coin_sequences)), coin_sequences)
    
    # Add text annotations in each cell
    for i in range(len(results)):
        for j in range(len(coin_sequences)):
            text = f'{results_array[i, j]:.4f}'
            plt.text(j, i, text, ha='center', va='center')
    
    plt.title(title)
    plt.xlabel('Sequence 2')
    plt.ylabel('Sequence 1')
    
    # Adjust layout
    plt.tight_layout()
    
    return plt

plot = plot_sequence_heatmap(coin_sequences, results)
plt.show()