#python3
import sys
def number_of_components(adj):
    lis = [False]*len(adj)
    c = 0
    #write your code here
    def explore(i, lis):
        lis [i] = True
        #print(lis)
        for i in adj[i][:]:
            if lis[i] == False:
                explore(i, lis)
    for i in range(len(adj)):
        if lis [i] == False:
            c = c + 1
            explore(i,lis)
    #print(lis)
    return c

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))