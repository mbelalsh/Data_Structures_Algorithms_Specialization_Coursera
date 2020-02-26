#python3
import sys

def reach(adj, x, y):
    lis = [False]*len(adj)
    #write your code here
    def explore(i, lis):
        lis [i] = True
        #print(lis)
        for i in adj[i][:]:
            if lis[i] == False:
                explore(i, lis)
    explore(x,lis)
    #print(lis)
    if lis[y] == True:
        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))