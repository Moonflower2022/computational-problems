import random


class SquareLine:  # white is 1 and black is 0; assuming that at the start all white squares are free
    def __init__(self, squares):
        self.squares = squares
        self.num_squares = len(squares)
        self.free_whites = [
            index for index, square in enumerate(squares) if square == 1
        ]
        random.shuffle(self.free_whites)

    def in_line(self, index):
        return 0 <= index < self.num_squares

    def color_black(self, index):
        self.squares[index] = 0
        if index in self.free_whites:
            self.free_whites.remove(index)
        if (
            self.in_line(index + 1)
            and (index + 1) in self.free_whites
            and self.in_line(index + 2)
            and self.squares[index + 2] == 0
        ):
            self.free_whites.remove(index + 1)
        if (
            self.in_line(index - 1)
            and (index - 1) in self.free_whites
            and self.in_line(index - 2)
            and self.squares[index - 2] == 0
        ):
            self.free_whites.remove(index - 1)

    def count_whites(self):
        return sum(self.squares)

def num_whites_remaining(n):
    squares = [0] + [1] * n + [0]

    square_line = SquareLine(squares)

    while len(square_line.free_whites) > 0:
        random_free_white = square_line.free_whites[-1]
        direction = 1 if random.random() < 0.5 else -1
        square_line.color_black(random_free_white + direction)
        
    return square_line.count_whites()


def W(n, iterations):
    return sum([num_whites_remaining(n) for _ in range(iterations)]) / iterations


if __name__ == "__main__":
    test_ns = (
        list(range(10, 40, 10)) + list(range(1000, 4000, 1000))
    )
    iterations = 1000
    for test_n in test_ns:
        avg_num_whites_remaining = W(test_n, iterations)
        print(test_n, avg_num_whites_remaining, avg_num_whites_remaining / test_n)
