import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

class SquareCoverageSimulation:
    def __init__(self):
        self.fixed_square_corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
        
    def rotate_square(self, center, angle):
        """Generate corners of a unit square centered at 'center' and rotated by 'angle'"""
        # Unit square centered at origin
        base_corners = np.array([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5]])
        
        # Rotation matrix
        cos_a, sin_a = np.cos(angle), np.sin(angle)
        rotation_matrix = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
        
        # Rotate and translate
        rotated_corners = np.dot(base_corners, rotation_matrix.T) + center
        return rotated_corners
    
    def point_in_polygon(self, point, polygon):
        """Check if a point is inside a polygon using ray casting algorithm"""
        x, y = point
        n = len(polygon)
        inside = False
        
        p1x, p1y = polygon[0]
        for i in range(1, n + 1):
            p2x, p2y = polygon[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        
        return inside
    
    def covers_any_corner(self, center, angle):
        """Check if the rotated square covers any corner of the fixed square"""
        rotated_corners = self.rotate_square(center, angle)
        
        for corner in self.fixed_square_corners:
            if self.point_in_polygon(corner, rotated_corners):
                return True
        return False
    
    def run_simulation(self, n_trials=100000):
        """Run Monte Carlo simulation"""
        print(f"Running simulation with {n_trials:,} trials...")
        
        covers_count = 0
        
        for i in range(n_trials):
            # Random center within unit square
            center = np.random.uniform(0, 1, 2)
            # Random rotation between 0 and π/2
            angle = np.random.uniform(0, np.pi/2)
            
            if self.covers_any_corner(center, angle):
                covers_count += 1
            
            if (i + 1) % 10000 == 0:
                current_prob = covers_count / (i + 1)
                print(f"Trial {i+1:,}: Current probability = {current_prob:.4f}")
        
        probability = covers_count / n_trials
        std_error = np.sqrt(probability * (1 - probability) / n_trials)
        
        print(f"\nFinal Results:")
        print(f"Trials: {n_trials:,}")
        print(f"Covers any corner: {covers_count:,}")
        print(f"Probability: {probability:.6f} ± {1.96*std_error:.6f}")
        
        return probability, std_error
    
    def visualize_examples(self, n_examples=20):
        """Create visualization showing examples of the simulation"""
        fig, axes = plt.subplots(4, 5, figsize=(15, 12))
        axes = axes.flatten()
        
        fig.suptitle('Random Examples: Unit Square Coverage Simulation\n' + 
                    'Fixed square (blue) vs Rotated square (red=covers corner, green=no coverage)', 
                    fontsize=14)
        
        for i in range(n_examples):
            ax = axes[i]
            
            # Random parameters
            center = np.random.uniform(0, 1, 2)
            angle = np.random.uniform(0, np.pi/2)
            
            # Check if it covers any corner
            covers = self.covers_any_corner(center, angle)
            rotated_corners = self.rotate_square(center, angle)
            
            # Plot fixed square
            fixed_square = Polygon(self.fixed_square_corners, fill=False, 
                                 edgecolor='blue', linewidth=2, label='Fixed square')
            ax.add_patch(fixed_square)
            
            # Plot rotated square
            color = 'red' if covers else 'green'
            alpha = 0.3 if covers else 0.1
            rotated_square = Polygon(rotated_corners, fill=True, facecolor=color, 
                                   alpha=alpha, edgecolor=color, linewidth=2)
            ax.add_patch(rotated_square)
            
            # Plot corners of fixed square
            for corner in self.fixed_square_corners:
                ax.plot(corner[0], corner[1], 'bo', markersize=6)
            
            # Plot center of rotated square
            ax.plot(center[0], center[1], 'ko', markersize=4)
            
            ax.set_xlim(-0.5, 1.5)
            ax.set_ylim(-0.5, 1.5)
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            ax.set_title(f'θ={angle:.2f}, Covers: {covers}', fontsize=10)
        
        plt.tight_layout()
        plt.show()
    
    def interactive_visualization(self):
        """Create an interactive visualization to manually test cases"""
        fig, ax = plt.subplots(figsize=(10, 8))
        plt.subplots_adjust(bottom=0.2)
        
        # Initial parameters
        center = np.array([0.5, 0.5])
        angle = 0.0
        
        def update_display():
            ax.clear()
            
            # Check coverage
            covers = self.covers_any_corner(center, angle)
            rotated_corners = self.rotate_square(center, angle)
            
            # Plot fixed square
            fixed_square = Polygon(self.fixed_square_corners, fill=False, 
                                 edgecolor='blue', linewidth=3, label='Fixed square')
            ax.add_patch(fixed_square)
            
            # Plot rotated square
            color = 'red' if covers else 'green'
            alpha = 0.3 if covers else 0.1
            rotated_square = Polygon(rotated_corners, fill=True, facecolor=color, 
                                   alpha=alpha, edgecolor=color, linewidth=3, 
                                   label=f'Rotated square ({"covers" if covers else "no coverage"})')
            ax.add_patch(rotated_square)
            
            # Plot corners and center
            for i, corner in enumerate(self.fixed_square_corners):
                ax.plot(corner[0], corner[1], 'bo', markersize=8, 
                       label='Fixed corners' if i == 0 else "")
            
            ax.plot(center[0], center[1], 'ko', markersize=6, label='Rotation center')
            
            ax.set_xlim(-0.7, 1.7)
            ax.set_ylim(-0.7, 1.7)
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_title(f'Interactive Test: Center=({center[0]:.2f}, {center[1]:.2f}), ' + 
                        f'Angle={angle:.2f} rad ({np.degrees(angle):.1f}°)\n' + 
                        f'Covers any corner: {covers}', fontsize=12)
            
            plt.draw()
        
        def on_click(event):
            nonlocal center
            if event.inaxes == ax and event.button == 1:  # Left click
                center = np.array([event.xdata, event.ydata])
                update_display()
        
        def on_key(event):
            nonlocal angle
            if event.key == 'left':
                angle = max(0, angle - 0.1)
                update_display()
            elif event.key == 'right':
                angle = min(np.pi/2, angle + 0.1)
                update_display()
        
        fig.canvas.mpl_connect('button_press_event', on_click)
        fig.canvas.mpl_connect('key_press_event', on_key)
        
        # Add instructions
        plt.figtext(0.1, 0.05, 'Instructions: Click to move center, Use ← → arrows to rotate', 
                   fontsize=10)
        
        update_display()
        plt.show()

def main():
    sim = SquareCoverageSimulation()
    
    print("Unit Square Corner Coverage Simulation")
    print("=" * 50)
    print("Problem: What's the probability that a unit square with:")
    print("- Center uniformly distributed in [0,1] × [0,1]")
    print("- Uniform rotation in [0, π/2]")
    print("covers any corner of the fixed unit square [0,1] × [0,1]?")
    print()
    
    # Run simulation
    prob, error = sim.run_simulation(100000)
    
    # Show examples
    print("\nGenerating visualization with random examples...")
    sim.visualize_examples()
    
    # Interactive mode
    print("\nStarting interactive visualization...")
    print("Click to move the center, use arrow keys to rotate!")
    sim.interactive_visualization()

if __name__ == "__main__":
    main()