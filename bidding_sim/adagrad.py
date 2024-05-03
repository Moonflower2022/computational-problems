# gradient descent optimization with adagrad for a two-dimensional test function
from math import sqrt
from numpy import asarray
from numpy.random import rand
from numpy.random import seed
import autograd.numpy as np
from autograd import elementwise_grad

l = 0.1
n = 2

def f(x):
    return (100 - x) * n * (1 - np.exp(-l * x)) ** (n - 1) * l * np.exp(-l * x) - (1 - np.exp(-l * x)) ** n

def objective(x):
    return f(x) ** 2

# gradient descent algorithm with adagrad
def adagrad(objective, derivative, bounds, n_iter, step_size):
	# generate an initial point
	solution = np.array([50.])
	# list of the sum square gradients for each variable
	sq_grad_sums = [0.0 for _ in range(bounds.shape[0])]
	# run the gradient descent
	for it in range(n_iter):
		# calculate gradient
		gradient = derivative(solution)
		# update the sum of the squared partial derivatives
		for i in range(gradient.shape[0]):
			sq_grad_sums[i] += gradient[i]**2.0
		# build a solution one variable at a time
		new_solution = list()
		for i in range(solution.shape[0]):
			# calculate the step size for this variable
			alpha = step_size / (1e-8 + sqrt(sq_grad_sums[i]))
			# calculate the new position in this variable
			value = solution[i] - alpha * gradient[i]
			# store this variable
			new_solution.append(value)
		# evaluate candidate point
		solution = asarray(new_solution)
		solution_eval = objective(solution)
		# report progress
		print(f'{it}: f({solution}) = {solution_eval}', end="\r")
	return [solution, solution_eval]

seed(42)

bounds = asarray([[0], [100]])

n_iter = 100000
step_size = 0.1

derivative = elementwise_grad(objective)

best, score = adagrad(objective, derivative, bounds, n_iter, step_size)
print('Done!')
print(f'f({best}) = {score}')