# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def findTrimmedRoot(self, root, L, R):
        from collections import deque
        Q = deque([root])
        while len(Q):
            n = Q.popleft()
            if L <= n.val <= R:
                return n
            else:
                if n.left is not None:
                    Q.append(n.left)

                if n.right is not None:
                    Q.append(n.right)

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        trimmed_root = self.findTrimmedRoot(root, L, R)

        if trimmed_root is not None:
            trimmed_root.left = self.trimBST(trimmed_root.left, L, R)
            trimmed_root.right = self.trimBST(trimmed_root.right, L, R)

        return trimmed_root


s = Solution()

t = TreeNode(3)
t.left = TreeNode(0)
t.right = TreeNode(4)
t.left.right = TreeNode(2)
t.left.right.left = TreeNode(1)

s.trimBST(t, 1, 3)


