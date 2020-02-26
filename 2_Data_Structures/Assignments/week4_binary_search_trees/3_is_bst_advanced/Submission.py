#!/usr/bin/python3
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(k, mini, maxi):
  if not k in tree:
    return True
  if tree[k][0] < mini or tree[k][0] > maxi:
    return False
  return IsBinarySearchTree(tree[k][1], mini, tree[k][0] - 1)  and IsBinarySearchTree(tree[k][2], tree[k][0], maxi)

def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree, int_max, int_min = {}, 2147483647, -2147483648
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0, int_min, int_max):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target = main).start()