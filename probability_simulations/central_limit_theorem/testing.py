import random
import numpy as np
import matplotlib.pyplot as plt

def get_normal(n):
    return random.normalvariate(0, 1)

def get_scaled_exponential_mean(n):
    mean = 1
    standard_deviation = 1
    return standard_deviation * (float(np.mean(np.random.exponential(1, n))) - mean) * (n ** (1/2))

def get_scaled_uniform_mean(n):
    mean = 0.5
    standard_deviation = 12 ** (1/2)
    return standard_deviation * (float(np.mean(np.random.random(n))) - mean) * (n ** (1/2))

def get_scaled_cauchy_mean(n):
    return float(np.mean(np.random.standard_cauchy(n))) * (n ** (1/2))

def plot_histogram(n, iterations, sample_function):
    sample_means = [sample_function(n) for _ in range(iterations)]

    plt.hist(sample_means, bins=100)
    plt.show()

if __name__ == "__main__":
    n = 10000
    iterations = 10000

    # plot_histogram(n, iterations, get_normal)
    # plot_histogram(n, iterations, get_scaled_uniform_mean)
    plot_histogram(n, iterations, get_scaled_exponential_mean)
    # plot_histogram(n, iterations, get_scaled_cauchy_mean)
    