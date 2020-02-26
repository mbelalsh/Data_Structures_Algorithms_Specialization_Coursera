#python3
import sys
def number_of_strongly_connected_components(adj):
    lis = [False]*len(adj)
    global c
    c = 0
    #write your code here
    def explore(i,rem, lis):
        global c
        lis [i] = True
        #print(rem)
        for i in adj[i][:]:
            #print(i)
            if lis[i] == False:
                explore(i,rem,lis)
            elif lis[i] == True and i == rem:
                    #print("java")
                    c += 1
    for i in range(len(adj)):
        #print('Bilal')
        if lis [i] == False:
            rem = i
            explore(i,rem,lis)
    if c >= 1:
        return 1
    #print(lis)
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))