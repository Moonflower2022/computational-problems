import random
import time


class SquareLine:
    def __init__(self, squares):
        self.squares = squares
        self.num_squares = len(squares)
        self.free_whites = set([index for index, square in enumerate(squares) if square == 1])

    def in_line(self, index):
        return 0 <= index < self.num_squares

    def color_black(self, index):
        self.squares[index] = 0
        
        if index in self.free_whites:
            self.free_whites.remove(index)
            
        # Check if adjacent white square now has a black square on both sides
        if (self.in_line(index + 1) and (index + 1) in self.free_whites
                and self.in_line(index + 2) and self.squares[index + 2] == 0):
            self.free_whites.remove(index + 1)
            
        if (self.in_line(index - 1) and (index - 1) in self.free_whites
                and self.in_line(index - 2) and self.squares[index - 2] == 0):
            self.free_whites.remove(index - 1)

    def count_whites(self):
        return sum(self.squares)


def num_whites_remaining(n):
    squares = [0] + [1] * n + [0]
    square_line = SquareLine(squares)

    while square_line.free_whites:
        random_free_white = random.choice(list(square_line.free_whites))
        direction = 1 if random.random() < 0.5 else -1
        square_line.color_black(random_free_white + direction)
        
    return square_line.count_whites()


def W(n, iterations):
    return sum(num_whites_remaining(n) for _ in range(iterations)) / iterations


if __name__ == "__main__":
    test_ns = list(range(10, 40, 10)) + list(range(1000, 4000, 1000))
    iterations = 1000
    
    start_time = time.time()
    
    for test_n in test_ns:
        iter_start = time.time()
        avg_num_whites_remaining = W(test_n, iterations)
        iter_end = time.time()
        
        print(f"n={test_n}, avg_whites={avg_num_whites_remaining:.2f}, ratio={avg_num_whites_remaining/test_n:.4f}, time={iter_end-iter_start:.2f}s")
    
    end_time = time.time()
    print(f"\nTotal runtime: {end_time - start_time:.2f} seconds")