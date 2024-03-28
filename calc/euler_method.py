def step(x, y, slope_func, step_size):
    return y + slope_func(x, y) * step_size

def euler_method(x0, y0, slope_func, stop_x, iterations, only_last_y=True):
    assert x0 < stop_x
    
    step_size = (stop_x - x0) / iterations

    x_list = [x0 + i * step_size for i in range(iterations)]
    y_list = [y0]

    print(iterations)

    for i in range(iterations):
        y_list.append(step(x_list[i], y_list[i], slope_func, step_size))


    if only_last_y:
        return y_list[-1]
    return y_list

def euler_method_step_size(x0, y0, slope_func, stop_x, step_size, only_last_y=True):
    iterations = int((stop_x - x0) / step_size)
    return euler_method(x0, y0, slope_func, stop_x, iterations, only_last_y=only_last_y)


def my_slope_func(x, y):
    return x + y + 1

print(euler_method_step_size(2, -1, my_slope_func, 2.6, 0.3))