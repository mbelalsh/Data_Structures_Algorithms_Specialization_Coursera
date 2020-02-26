# Uses python3
import sys
import itertools

def partition3(A):
    a = len(A)
    sum_a = sum(A)
    if sum_a % 3 != 0:
        return 0
    else:
        div = sum_a // 3
        L = [[False for i in range(div + 1)] for i in range(a + 1)]
        for i in range(a + 1):
            L[i][0] = True
        for i in range(1, div + 1):
            L[0][i] = False
        for i in range(1, a + 1):
            for j in range(1, div + 1):
                if A[i - 1] > j:
                    L[i][j] = L[i - 1][j]
                if A[i - 1] <= j:
                    L[i][j] = L[i - 1][j] or L[i - 1][j - A[i - 1]]
        ans = L[-1][-1]
        if ans:
            return 1
        else:
            return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

