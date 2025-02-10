import random
import matplotlib.pyplot as plt

def simulate(n):
    total = 0
    while total < n:
        total += random.randint(1, 6)
    if total == n:
        return True
    return False

def test_one_n(n):
    n = 7
    iterations = 1000000
    total_good = 0
    for i in range(iterations):
        if simulate(n):
            total_good += 1

    print("observed ratio:", total_good / iterations)

def plot_distribution():
    ns = range(1, 100)  # Test values for n
    iterations = 100000  # Reduce for faster execution
    observed_ratios = []

    for n in ns:
        total_good = sum(1 for _ in range(iterations) if simulate(n))
        observed_ratios.append(total_good / iterations)

    plt.figure(figsize=(10, 5))
    plt.plot(ns, observed_ratios, label="Observed", marker="o")
    plt.xlabel("n")
    plt.ylabel("Probability")
    plt.title("Observed vs Expected Probability Distribution")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_distribution()
    