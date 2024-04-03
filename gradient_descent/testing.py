import autograd.numpy as np
from autograd.differential_operators import jacobian

fun = lambda x: np.sin(x)

print("fun(np.array([1, 2])):", fun(np.array([1, 2])))

jacobian_matrix = jacobian(fun)

random = np.random.randn(2)

print(random)

print(jacobian_matrix(random))

array = np.array([1, 2], dtype=np.float64) # it doesnt work with np.int64 for some reason

print(array)

print(jacobian_matrix(array))