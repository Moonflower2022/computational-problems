import random
import matplotlib.pyplot as plt
import numpy as np

def generate_points(x1, y1, x2, y2, num_points):
    slope = (y1 - y2) / (x1 - x2)
    def line(x):
        return y1 + slope * (x - x1)
    

    x_for_y0 = -y1 / slope + x1
    x_for_y1 = (1 - y1) / slope + x1
    if x_for_y0 < 0: 
        x_for_y0 = 0
    if x_for_y0 > 1:
        x_for_y0 = 1
    if x_for_y1 < 0:
        x_for_y1 = 0
    if x_for_y1 > 1:
        x_for_y1 = 1

    distance = abs(x_for_y0 - x_for_y1)

    xs = []
    ys = []
    for i in range(num_points):
        x = min(x_for_y0, x_for_y1) + distance/num_points * i
        y = line(x)
        if 0 < x < 1 and 0 < y < 1:
            xs.append(x)
            ys.append(y)
    return xs, ys

def plot_lines():
    all_xs = []
    all_ys = []
    iterations = 1000
    num_points = 1000
    for _ in range(iterations):
        x1 = random.random()
        y1 = random.random()
        x2 = random.random()
        y2 = random.random()
        xs, ys = generate_points(x1, y1, x2, y2, num_points)

        all_xs += xs
        all_ys += ys

    
    
    plt.scatter(all_xs, all_ys, s=0.01)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()

def plot_heatmap():
    all_xs = []
    all_ys = []
    iterations = 100000
    num_points = 1000
    for _ in range(iterations):
        x1 = random.random()
        y1 = random.random()
        x2 = random.random()
        y2 = random.random()
        xs, ys = generate_points(x1, y1, x2, y2, num_points)

        all_xs += xs
        all_ys += ys
    # Create 2D histogram (heatmap)
    bins = 20  # Creates 10x10 grid (100 squares)
    heatmap, xedges, yedges = np.histogram2d(all_xs, all_ys, bins=bins, range=[[0, 1], [0, 1]])

    # Plot heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(heatmap.T, origin='lower', extent=[0, 1, 0, 1], cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Number of Points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Point Density Heatmap')
    plt.show()

if __name__ == "__main__":
    plot_heatmap()