import autograd.numpy as np
from autograd import grad

A = np.array([[1, 2], [3, 4]])
B = np.array([3, 2])

def objective(x):
    return np.linalg.norm(np.dot(A, x) - B) ** 2

gradient = grad(objective)

point = np.array([0, 0])

iterations = 100000
learning_rate = 0.001

for i in range(iterations):
    point = point - learning_rate * gradient(point)

print("local minimum:", point)
print("error |Ax - b|^2:", objective(point))
print("Ax - b:", np.dot(A, point) - B)

# 1x_1 + 2x_2 = 3
# 3x_1 + 4x_2 = 2