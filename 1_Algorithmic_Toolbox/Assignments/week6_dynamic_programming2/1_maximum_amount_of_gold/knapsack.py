# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    w_len = len(w)
    L = [[0] * (W + 1) for i in range(w_len + 1)]
    for i in range(1, w_len + 1):
        for j in range(1, W + 1):
            k = i - 1
            if w[k] > j:
                L[i][j] = L[i - 1][j]
            elif L[i - 1][j - w[k]] + w[k] <= j:
                L[i][j] = max(L[i - 1][j - w[k]] + w[k], L[i - 1][j])
            else:
                L[i][j] = L[i - 1][j]
    return L[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
