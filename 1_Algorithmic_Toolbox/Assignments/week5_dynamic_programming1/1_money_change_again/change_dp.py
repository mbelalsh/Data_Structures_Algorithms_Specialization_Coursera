# Uses python3
import sys

def get_change(m):
    #write your code here
    table = [0] * (m + 1)
    if m == 1:
        table[1] = 1
    elif m == 2:
        table[1] = 1
        table[2] = 2
    elif m == 3:
        table[1] = 1
        table[2] = 2
        table[3] = 1
    elif m == 4:
        table[1] = 1
        table[2] = 2
        table[3] = 1
        table[4] = 1
    elif m > 4:
        table[1] = 1
        table[2] = 2
        table[3] = 1
        table[4] = 1
        for i in range(5, m + 1):
            minCoin = min(table[i - 3], table[i - 1], table[i - 4])
            table[i] = minCoin + 1
    return table[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
