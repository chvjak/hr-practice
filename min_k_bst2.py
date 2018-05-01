'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''

'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k
'''


# your task is to complete this function
# function should return kth smallest element from the BST
def k_smallest_element(root, n):
    # Code here

    def dfs(root):
        nonlocal k, res
        if k >= n:
            return

        if root is None:
            return

        if root.left is not None:
            dfs(root.left)

        k += 1

        if k == n:
            res = root.data

        if root.right is not None:
            dfs(root.right)

    k = 0
    res = None

    dfs(root)

    return res


def func1():
    a = 10

    def func2():
        a.__iadd__(3)

        print(a)

    func2()

func1()