# Uses python3
import sys

def get_change(m):
    #write your code here
    i = 0
    j = 0
    while i < m:
        if i + 10 <= m:
            i += 10
            j += 1
        elif i + 5 <= m:
            i += 5
            j += 1
        else:
            i += 1
            j += 1
    return j

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
