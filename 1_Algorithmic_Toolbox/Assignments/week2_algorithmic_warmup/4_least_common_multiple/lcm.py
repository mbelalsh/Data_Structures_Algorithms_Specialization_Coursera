# Uses python3
import sys

def lcm_naive(a, b):
    m = a * b
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return int(m / a)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

