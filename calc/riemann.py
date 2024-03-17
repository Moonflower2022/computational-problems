import numpy as np
import math
import matplotlib.pyplot as plt

def riemann_left(func, a, b, n, pos=False):
    delta_x = (b - a)/n
    if not pos:
        return sum(func(a + i*delta_x) for i in range(0, n))*delta_x
    return sum(abs(func(a + i*delta_x)) for i in range(0, n))*delta_x

def riemann_middle(func, a, b, n, pos):
    delta_x = (b - a)/n
    if not pos:
        return sum(func(a + delta_x/2 + i*delta_x) for i in range(0, n))*delta_x
    return sum(abs(func(a + delta_x/2 + i*delta_x)) for i in range(0, n))*delta_x

def riemann_right(func, a, b, n, pos):
    delta_x = (b - a)/n
    if not pos:
        return sum(func(a + i*delta_x) for i in range(1, n + 1))*delta_x
    return sum(abs(func(a + i*delta_x)) for i in range(1, n + 1))*delta_x

def riemann_trapezoid(func, a, b, n, pos):
    delta_x = (b - a)/n
    if not pos:
        return sum((func(a + i*delta_x) + func(a + (i+1)*delta_x))/2 for i in range(0, n))*delta_x
    return sum(abs((func(a + i*delta_x) + func(a + (i+1)*delta_x))/2) for i in range(0, n))*delta_x

'''
def func(x):
    return math.sin(math.pi/x) ** 2
func_description = "sin^2(pi/x)"
'''
def func(x):
    return math.exp(x)
func_description = "e^x"



left = 0
right = 1
n_values = [10**(i+1) for i in range(7)]
# list(range(1, 50))
print(n_values)
print_last = True
pos = False

func_list = [
    #riemann_left, 
    riemann_middle, 
    riemann_right, 
    #riemann_trapezoid
]
matrix = np.zeros((len(func_list), len(n_values)))

for i in range(len(n_values)): 
    for j in range(len(func_list)):
        result = func_list[j](func, left, right, n_values[i], pos)
        matrix[j][i] = result
        if print_last and i == len(n_values) - 1:
            print(f"{func_list[j].__name__} at {n_values[i]}: {result}")

for j in range(len(func_list)):
    plt.plot(n_values, matrix[j], label=func_list[j].__name__)

plt.xlabel('n')
plt.ylabel('Area Approximation')
plt.title(f'{"geometric" if pos else "signed"} area between y = {func_description} and the x-axis from {left} to {right}')
plt.xscale('log')  # Use logarithmic scale for x-axis
plt.legend()
plt.grid(True)
plt.show()