import random
import matplotlib.pyplot as plt
import numpy as np

def generate_points(x1, y1, x2, y2, num_points):    
    slope = (y2 - y1) / (x2 - x1)
    
    def line(x):
        return y1 + slope * (x - x1)
    
    # Find intersections with unit square boundaries
    intersections = []
    
    # Check intersection with x = 0
    if 0 <= line(0) <= 1:
        intersections.append((0, line(0)))
    
    # Check intersection with x = 1
    if 0 <= line(1) <= 1:
        intersections.append((1, line(1)))
    
    # Check intersection with y = 0 (if slope != 0)
    if abs(slope) > 1e-10:
        x_at_y0 = x1 - y1 / slope
        if 0 <= x_at_y0 <= 1:
            intersections.append((x_at_y0, 0))
    
    # Check intersection with y = 1 (if slope != 0)
    if abs(slope) > 1e-10:
        x_at_y1 = x1 + (1 - y1) / slope
        if 0 <= x_at_y1 <= 1:
            intersections.append((x_at_y1, 1))
    
    # Remove duplicates and ensure we have exactly 2 intersections
    intersections = list(set(intersections))
    
    if len(intersections) < 2:
        return [], []
    
    # Take first two intersections
    (x_start, y_start), (x_end, y_end) = intersections[:2]
    
    # Generate points along the line segment
    xs = []
    ys = []
    for i in range(num_points):
        t = i / (num_points - 1) if num_points > 1 else 0
        x = x_start + t * (x_end - x_start)
        y = y_start + t * (y_end - y_start)
        xs.append(x)
        ys.append(y)
    
    return xs, ys

def plot_heatmap():
    all_xs = []
    all_ys = []
    iterations = 10000  # Reduced for testing
    num_points = 1000    # Reduced for testing
    
    for i in range(iterations):
        if i % 1000 == 0:
            print(f"Progress: {i}/{iterations}")
            
        x1 = random.random()
        y1 = random.random()
        x2 = random.random()
        y2 = random.random()
        xs, ys = generate_points(x1, y1, x2, y2, num_points)
        
        all_xs += xs
        all_ys += ys
    
    print(f"Generated {len(all_xs)} points")
    
    # Create 2D histogram (heatmap)
    bins = 20
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