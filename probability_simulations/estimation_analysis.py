import numpy as np

def maximum_likelihood_normal(num_samples):
    # assume we have a r.v. X ~ N(0, 1)

    samples = np.random.normal(0, 1, num_samples)

    mean = np.mean(samples)

    sample_variance = np.sum(np.pow(samples - mean, 2)) / (num_samples - 1)

    return np.array(np.abs([mean, sample_variance - 1]))

def maximum_likelihood_normal_average(testing_function, num_samples, num_iterations):
    return np.sum([testing_function(num_samples) for _ in range(num_iterations)], axis=0) / num_iterations


def maximum_likelihood_normal_vectorized(num_samples, num_iterations): # Source: Claude 3.7 Sonnet
    actual_mean = 10
    # Generate all samples at once as a 2D array
    all_samples = np.random.normal(actual_mean, 1, (num_iterations, num_samples))
    
    # Calculate means for each iteration (across each row)
    means = np.mean(all_samples, axis=1)
    
    # Calculate sample variances efficiently
    centered = all_samples - means[:, np.newaxis]  # Subtract mean from each row
    sample_variances = np.sum(centered**2, axis=1) / (num_samples - 1)
    
    # Calculate absolute differences and take average across iterations
    abs_mean_diff = np.abs(means - actual_mean)
    abs_var_diff = np.abs(sample_variances - 1)
    
    return np.array([np.mean(abs_mean_diff), np.mean(abs_var_diff)])

def conjugate_prior_normal(num_samples, num_iterations):
    actual_mean = 10

    # Generate all samples at once as a 2D array
    all_samples = np.random.normal(actual_mean, 1, (num_iterations, num_samples))

    variance = 1

    mu_variance0 = 10000
    mu_mean0 = 0

    mu_variance1 = 1 / (1 / mu_variance0 + num_samples / variance)
    mean1 = mu_variance1 * (np.sum(all_samples, axis=1) / variance + mu_mean0 / mu_variance0)

    return np.mean(np.abs(mean1 - actual_mean))

if __name__ == "__main__":
    print(maximum_likelihood_normal_vectorized(100, 10000000))
    result = conjugate_prior_normal(100, 10000000)
    print(result)

