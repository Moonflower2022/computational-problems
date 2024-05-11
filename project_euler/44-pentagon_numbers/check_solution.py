def main():
    pentagon_numbers = [generate_pentagon_number(i) for i in range(1, 1000000)]
    print(check_solution(pentagon_numbers, 3, 5))


def check_solution(pentagon_numbers, p_i, p_j):
    if (abs(p_i - p_j) in pentagon_numbers) and (p_i + p_j in pentagon_numbers):
        return True
    return False


def generate_pentagon_number(n):
    return n * (3 * n - 1) // 2


if __name__ == "__main__":
    main()