import numpy as np
import math
import matplotlib.pyplot as plt

def dot_spread(func, left, right, lower_bound, upper_bound, n, pos):
    area = (right - left) * (upper_bound - lower_bound)

    x = np.random.uniform(left, right, n)
    y = np.random.uniform(lower_bound, upper_bound, n)

    under_curve = np.logical_and(np.abs(y) <= np.abs(func(x)), np.sign(y) == np.sign(func(x)))

    if not pos:
        signed_points = y[under_curve]/np.abs(y[under_curve])
        return (np.count_nonzero(signed_points == 1) - np.count_nonzero(signed_points == -1))/n * area
    return np.count_nonzero(under_curve == True) / n * area




def func(x):
    return np.power(np.sin(np.pi/x), 2)
func_description = "sin^2(pi/x)"
'''

def func(x):
    return np.sin(np.pi/x)
func_description = "sin(pi/x)"
'''
'''
def func(x):
    return np.exp(x)
func_description = "e^x"
'''
# make sure func is vectorized


left = 0
right = 1
assert left < right

upper_bound = 1
lower_bound = -1
assert lower_bound < upper_bound
# we know this because the range of sin is [-1, 1]

n_values = [10**(i+1) for i in range(7)]
print(n_values)
print_last = True
pos = True

results = np.zeros(len(n_values))

for i, n in enumerate(n_values): 
    result = dot_spread(func, left, right, lower_bound, upper_bound, n, pos)
    results[i] = result
    if print_last and i == len(n_values) - 1:
        print(f"{n}: {result}")

plt.plot(n_values, results)

plt.xlabel('Dots')
plt.ylabel('Area Approximation')
plt.title(f'approximated {"geometric" if pos else "signed"} area between y = {func_description} and the x-axis from {left} to {right}')
plt.xscale('log')  # Use logarithmic scale for x-axis
plt.grid(True)
plt.show()