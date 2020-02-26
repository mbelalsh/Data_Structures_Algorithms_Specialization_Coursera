#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    #res = 0
    #for i in range(len(a)):
    #    res += a[i] * b[i]
    #return res
    sorted_lis1 = sorted(a, reverse=True)
    sorted_lis2 = sorted(b, reverse=True)
    cum = 0
    for i in range(len(a)):
        cum += sorted_lis1[i] * sorted_lis2[i]
    return cum
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
