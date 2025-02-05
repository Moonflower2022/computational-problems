import random

def run_simulation(num_chips, num_cookies):
    cookie_indices = [random.randint(0, num_cookies - 1) for _ in range(num_chips)]

    for i in range(num_cookies):
        if not i in cookie_indices:
            return False
        
    return True

if __name__ == "__main__":
    num_chips = 690
    num_cookies = 100

    iterations = 100000

    total_success = 0
    for _ in range(iterations):
        if run_simulation(num_chips, num_cookies):
            total_success += 1
    print(total_success/iterations)

"""
**sage script:**

def f(x):
    return sum(binomial(100, n) * ((100 - n) / 100) ** x * (-1) ** (n + 1) for n in range(1, 100))

plot_f = plot(f(x), (x, 100, 1000), ymin=0, ymax=1, axes_labels=['x', 'f(x)'])
show(plot_f)
"""

"""
[(n, f(n).n()) for n in range(650, 700)]
"""
