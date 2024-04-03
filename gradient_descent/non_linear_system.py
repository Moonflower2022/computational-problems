import autograd.numpy as np
from autograd.differential_operators import jacobian

def f(x):
    num1 = 3 * x[0] - np.cos(x[1] * x[2]) - 3/2
    num2 = 4 * x[0] ** 2 - 625 * x[1] ** 2 + 2 * x[1] - 1
    num3 = np.exp(-x[0] * x[1]) + 20 * x[2] + (10 * np.pi - 3)/3
    return np.stack((num1, num2, num3), axis=0)

# system: Ax = B

def objective(x):
    num1 = 3 * x[0] - np.cos(x[1] * x[2]) - 3/2
    num2 = 4 * x[0] ** 2 - 625 * x[1] ** 2 + 2 * x[1] - 1
    num3 = np.exp(-x[0] * x[1]) + 20 * x[2] + (10 * np.pi - 3)/3
    return (num1 ** 2 + num2 ** 2 + num3 ** 2)/2

jacobian_matrix = jacobian(f)

point = np.array([0, 0, 0], dtype=np.float64)

iterations = 50000
learning_rate = 0.0001

for i in range(iterations):
    print(f"Iterations: {i}/{iterations}", end="\r")
    point = point - learning_rate * np.dot(jacobian_matrix(point).T, f(point))

print("local minimum:", point)
print("error:", objective(point))

# refer to non_linear_system.png