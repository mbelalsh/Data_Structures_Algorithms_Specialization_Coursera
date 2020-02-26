# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here REFER TO JUPYTER NOTEBOOK
    dic = {}
    for i in a:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
            if dic[i] > len(a) // 2:
                return 1
                # print(dic)
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
