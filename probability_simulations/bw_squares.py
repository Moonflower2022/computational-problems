import random
import time


class RandomSet:
    """A data structure that supports O(1) random selection and O(1) removal"""
    
    def __init__(self, iterable=None):
        self.elements = {}  # Maps value -> index in the list
        self.values = []    # List of values for O(1) random selection
        
        if iterable:
            for item in iterable:
                self.add(item)
    
    def add(self, item):
        """Add an item to the set in O(1) time"""
        if item not in self.elements:
            self.elements[item] = len(self.values)
            self.values.append(item)
    
    def remove(self, item):
        """Remove an item from the set in O(1) time"""
        if item in self.elements:
            # Get the index of the item to remove
            index = self.elements[item]
            last_item = self.values[-1]
            
            # Move the last element to the position of the removed element
            self.values[index] = last_item
            self.elements[last_item] = index
            
            # Remove the last element
            self.values.pop()
            del self.elements[item]
    
    def random_choice(self):
        """Return a random element in O(1) time"""
        if not self.values:
            raise IndexError("Cannot choose from an empty set")
        return random.choice(self.values)
    
    def __contains__(self, item):
        return item in self.elements
    
    def __len__(self):
        return len(self.values)
    
    def __bool__(self):
        return bool(self.values)


class SquareLine:
    def __init__(self, squares):
        self.squares = squares
        self.num_squares = len(squares)
        # Use our new RandomSet instead of a regular set
        self.free_whites = RandomSet(
            [index for index, square in enumerate(squares) if square == 1]
        )

    def in_line(self, index):
        return 0 <= index < self.num_squares

    def color_black(self, index):
        self.squares[index] = 0

        if index in self.free_whites:
            self.free_whites.remove(index)

        # Check if adjacent white square now has a black square on both sides
        if (
            self.in_line(index + 2)
            and self.squares[index + 2] == 0
            and self.in_line(index + 1)
            and (index + 1) in self.free_whites
        ):
            self.free_whites.remove(index + 1)

        if (
            self.in_line(index - 2)
            and self.squares[index - 2] == 0
            and self.in_line(index - 1)
            and (index - 1) in self.free_whites
        ):
            self.free_whites.remove(index - 1)

    def count_whites(self):
        return sum(self.squares)


def num_whites_remaining(n):
    squares = [0] + [1] * n + [0]
    square_line = SquareLine(squares)

    while square_line.free_whites:
        # Use our new O(1) random_choice method instead of random.choice(list(...))
        random_free_white = square_line.free_whites.random_choice()
        direction = 1 if random.random() < 0.5 else -1
        square_line.color_black(random_free_white + direction)

    return square_line.count_whites()


def W(n, iterations):
    return sum(num_whites_remaining(n) for _ in range(iterations)) / iterations


if __name__ == "__main__":
    test_ns = list(range(10, 30+1, 10)) + list(range(1000, 3000+1, 1000)) + list(range(10000, 20000+1, 10000))
    iterations = 1000

    start_time = time.time()

    for test_n in test_ns:
        iter_start = time.time()
        avg_num_whites_remaining = W(test_n, iterations)
        iter_end = time.time()

        print(
            f"n={test_n}, avg_remaining_whites={avg_num_whites_remaining:.2f}, ratio={avg_num_whites_remaining/test_n:.4f}, time={iter_end-iter_start:.2f}s"
        )

    end_time = time.time()
    print(f"\nTotal runtime: {end_time - start_time:.2f} seconds")