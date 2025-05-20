import numpy as np

def normal_testing(num_samples):
    # assume we have a r.v. X ~ N(0, 1)

    samples = np.random.normal(0, 1, num_samples)

    mean = np.mean(samples)

    sample_variance = np.sum(np.pow(samples - mean, 2)) / (num_samples - 1)

    return np.array(np.abs([mean, sample_variance - 1]))

def average_error(testing_function, num_samples, num_iterations):
    return np.sum([testing_function(num_samples) for _ in range(num_iterations)], axis=0) / num_iterations

if __name__ == "__main__":
    print(average_error(normal_testing, 10000, 10000))


