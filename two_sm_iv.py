# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(top_root, root, k):
    if root is None:
        return False

    res = findTarget(top_root, k - root.val, root)

    if res:
        return True
    else:
        if dfs(top_root, root.left, k):
            return True
        elif dfs(top_root, root.right, k):
            return True

    return False


def findTarget(root, k, not_this):
    if root is None:
        return False

    if root.val == k and root != not_this:
        return True

    rl = rr = False
    if root.left is not None and k < root.val:
        rl = findTarget(root.left, k, not_this)
    elif root.right is not None and k > root.val:
        rr = findTarget(root.right, k, not_this)

    return rl or rr


class Solution(object):

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = dfs(root, root, k)

        return res




S = Solution()

T = TreeNode(5)

T.left = TreeNode(3)
T.right = TreeNode(6)

T.left.left = TreeNode(2)
T.left.right = TreeNode(4)

T.right.right = TreeNode(6)


print(S.findTarget(T, 5))
print(S.findTarget(T, 16))
print(S.findTarget(T, 9))
print(S.findTarget(T, 28))