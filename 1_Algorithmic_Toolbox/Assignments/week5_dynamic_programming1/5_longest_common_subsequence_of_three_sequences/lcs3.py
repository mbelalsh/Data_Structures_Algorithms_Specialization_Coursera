#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    l, n, m = len(a), len(b), len(c)
    L = [[[0 for k in range(m + 1)] for j in range(n + 1)] for i in range(l + 1)]
    for i in range(l):
        for j in range(n):
            for k in range(m):
                if a[i] == b[j] == c[k]:
                    L[i + 1][j + 1][k + 1] = L[i][j][k] + 1
                else:
                    L[i + 1][j + 1][k + 1] = max(L[i + 1][j + 1][k],
                                                 L[i][j + 1][k + 1],
                                                 L[i + 1][j][k + 1])
    return L[i + 1][j + 1][k + 1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
