#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    n, m = len(a), len(b)
    L = [[0] * (m + 1) for k in range(n + 1)]
    for j in range(n):
        for k in range(m):
            if a[j] == b[k]:
                L[j + 1][k + 1] = L[j][k] + 1
            else:
                L[j + 1][k + 1] = max(L[j][k + 1], L[j + 1][k])
    return L[j + 1][k + 1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
