# python3
import sys
import threading


def compute_height(n, parents):
    class Node(object):
        """Node class that create nodes, their corresponding children and determine the
           tree height by height method"""

        def __init__(self, data):
            self.data = data
            self.children = []

        def add_child(self, obj):
            self.children.append(obj)

        def height(self, idx=0):
            if len(self.children) == 0:
                return 1
            else:
                return 1 + max(c.height() for c in self.children)

    # create n nodes instances and save them in an array
    nodes = [0] * n
    for i in range(n):
        nodes[i] = Node(i)

    # recognize root node and create child nodes corresponding to given parents nodes
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = nodes[child_index]
        else:
            nodes[parent_index].add_child(nodes[child_index])

    return root.height()

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
