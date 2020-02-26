# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
    cum = 1
    for i in range(1, n):
        a, b = b, (a + b) % 10
        cum += b ** 2
    return cum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
