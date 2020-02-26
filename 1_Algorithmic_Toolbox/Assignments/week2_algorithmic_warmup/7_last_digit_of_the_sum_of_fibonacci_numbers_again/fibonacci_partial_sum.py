# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if m == 0 and n == 1:
        return n
    elif m == 0 and n == 2:
        return n
    elif m == 1 and n == 2:
        return n
    elif m == 0 and n > 2:
        a, b = 0, 1
        cum = 1
        for x in range(1, n):
            a, b = b, (a + b) % 10
            cum += b
        return cum % 10
    else:
        a, b = 0, 1
        cum = 0
        i = 1
        for x in range(1, n):
            i += 1
            a, b = b, (a + b) % 10
            if i >= m:
                cum += b
        return cum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    m, n = map(int, input.split())
    print(fibonacci_partial_sum_naive(m, n))