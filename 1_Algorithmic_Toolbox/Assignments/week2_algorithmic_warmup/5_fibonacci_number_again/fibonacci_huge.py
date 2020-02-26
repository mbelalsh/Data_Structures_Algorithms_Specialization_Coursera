# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    lis = [0, 1]
    if n < 2:
        return n
    else:
        a, b = 0, 1
        i = 2
        c = True
        while c:
            i = i + 1
            a, b = b, (a + b)
            rem1 = a % m
            rem2 = b % m
            lis.append(rem2)
            if rem2 == 1 and rem1 == 0:
                pis_per = i - 2
                c = False
    ind = n % pis_per
    # print(lis, i, ind)
    return lis[ind]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
