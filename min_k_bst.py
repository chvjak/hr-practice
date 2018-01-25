f = open('min_k_bst.txt')
def input():
    return f.readline()

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def addBST(root, val):
    if val < root.val:
        if root.left is None:
            root.left = TreeNode(val)
        else:
            addBST(root.left, val)
    elif val > root.val:
        if root.right is None:
            root.right = TreeNode(val)
        else:
            addBST(root.right, val)


def printBST(root):
    if root is None:
        return
    else:
        print(root.val)
        printBST(root.left)
        printBST(root.right)


def inorderBST(root, params):
    if params['K'] == 0:
        return

    if root is None:
        params['min_found'] = True
        return

    inorderBST(root.left, params)
    if params['min_found'] == True and params['K'] > 0:
        params['sum'] += root.val
        params['K'] -= 1

    inorderBST(root.right, params)


T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    nodes = [int(x) for x in input().strip().split(' ')]
    K = int(input().strip())
    root = TreeNode(nodes[0])
    for n in nodes[1:]:
        addBST(root, n)

    # printBST(root)
    params = {'K': K, 'sum': 0, 'min_found': False}
    inorderBST(root, params)

    print(params['sum'])

