def step(x, y, slope_func, step_size):
    return y + slope_func(x, y) * step_size

def euler_method(x0, y0, slope_func, stop_x, iterations, only_last_y=True):
    assert x0 < stop_x
    
    step_size = (stop_x - x0) / iterations

    x_list = [x0 + i * step_size for i in range(iterations+1)]
    y_list = [y0]

    for i in range(iterations):
        y_list.append(step(x_list[i], y_list[i], slope_func, step_size))

    if only_last_y:
        return y_list[-1]
    return x_list, y_list

def euler_method_step_size(x0, y0, slope_func, stop_x, step_size, only_last_y=True):
    iterations = int((stop_x - x0) / step_size)
    return euler_method(x0, y0, slope_func, stop_x, iterations, only_last_y=only_last_y)


def my_slope_func(x, y):
    return x + y + 1

x0 = 2
y0 = -1
stop_x = 2.6
iterations = 25


x_list, y_list = euler_method(x0, y0, my_slope_func, stop_x, 15, only_last_y=False)

print("x_values:", x_list)
print("y_values:", y_list)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sizes = [5 + i*(30-5)/(len(x_list)-1) for i in range(len(x_list))]
plt.title("points in Euler's method approximation (the bigger the dot the later it is)")
plt.scatter(x_list, y_list, sizes)
plt.show()