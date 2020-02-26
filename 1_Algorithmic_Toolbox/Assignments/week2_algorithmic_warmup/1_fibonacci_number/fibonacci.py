# Uses python3
def calc_fib(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
    for i in range(1, n):
        a, b = b, (a + b)
    return b

n = int(input())
print(calc_fib(n))
