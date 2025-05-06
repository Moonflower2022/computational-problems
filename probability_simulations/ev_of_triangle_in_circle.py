import numpy as np
from time import time

def random_points_in_circle_vectorized(n, radius=1):
    """Generate n random points uniformly within a circle of given radius in a vectorized way."""
    # Generate random angles and radii for all points at once
    theta = np.random.uniform(0, 2 * np.pi, n)
    
    # For uniform distribution in a circle, we need to take square root of random radius
    r = radius * np.sqrt(np.random.uniform(0, 1, n))
    
    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    return np.column_stack((x, y))

def triangle_areas_vectorized(points):
    """Calculate areas for multiple triangles vectorized."""
    # Reshape the points array to group them into triangles
    # Each triangle consists of 3 points, each point is 2D (x,y)
    triangles = points.reshape(-1, 3, 2)
    
    # Extract the vertices for each triangle
    p1 = triangles[:, 0]
    p2 = triangles[:, 1]
    p3 = triangles[:, 2]
    
    # Calculate the area using the cross product method
    # For each triangle: 0.5 * |cross product|
    areas = 0.5 * np.abs(
        p1[:, 0] * (p2[:, 1] - p3[:, 1]) + 
        p2[:, 0] * (p3[:, 1] - p1[:, 1]) + 
        p3[:, 0] * (p1[:, 1] - p2[:, 1])
    )
    
    return areas

def run_simulation_vectorized(num_trials=1000000, batch_size=100000):
    """Run the simulation in batches using vectorized operations."""
    total_area = 0
    remaining_trials = num_trials
    
    while remaining_trials > 0:
        # Determine the batch size for this iteration
        current_batch = min(batch_size, remaining_trials)
        
        # Generate 3 random points for each trial in the batch
        points = random_points_in_circle_vectorized(current_batch * 3)
        
        # Calculate areas for all triangles in the batch
        areas = triangle_areas_vectorized(points)
        
        # Sum the areas
        total_area += np.sum(areas)
        
        # Update remaining trials
        remaining_trials -= current_batch
    
    return total_area / num_trials

def main():
    """Calculate the expected value through simulation and compare with analytical solution."""
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Run multiple simulations with increasing number of trials
    trials = [1000000000]
    for num_trials in trials:
        start_time = time()
        expected_area = run_simulation_vectorized(num_trials)
        end_time = time()
        
        print(f"Expected area with {num_trials} trials: {expected_area:.8f}")
        print(f"Time taken: {end_time - start_time:.3f} seconds")
        print()

if __name__ == "__main__":
    main()