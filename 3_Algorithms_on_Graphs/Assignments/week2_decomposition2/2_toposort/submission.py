#python3

import sys
def toposort(adj):
    global z
    z = 0
    lis = [False for x in range(len(adj))]
    top_sort = [0] * len(adj)

    def explore(i, lis):
        global z
        lis[i] = True
        for q in adj[i][:]:
            if lis[q] == False:
                explore(q, lis)
        z += 1
        top_sort[-1 * z] = i

    for i in range(len(adj)):
        if lis[i] == False:
            explore(i, lis)
    return top_sort

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #print(adj)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')