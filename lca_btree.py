# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_both(root, val1, val2):
    if root is None:
        return False, False, -1

    found_one_l, found_both_l, lca_l = find_both(root.left, val1, val2)
    found_one_r, found_both_r, lca_r = find_both(root.right, val1, val2)

    if found_both_l:
        return True, True, lca_l

    if found_both_r:
        return True, True, lca_r

    if found_one_l and found_one_r:
        return True, True, root.val
    elif found_one_l or found_one_r:
        if root.val == val1 or root.val == val2:
            return True, True, root.val
        else:
            return True, False, -1
    elif root.val == val1 or root.val == val2:
        if val1 == val2:
            return True, True, root.val
        else:
            return True, False, -1
    else:
        return False, False, -1


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        __, __, lca = find_both(A, B, C)

        return lca

t = TreeNode(1)

s = Solution()
print(s.lca(t, 1, 1))
print(s.lca(t, 2, 3))
print(s.lca(t, 2, 5))
print(s.lca(t, 4, 5))

