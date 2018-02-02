# Definition for a binary tree node.
# https://leetcode.com/problems/longest-univalue-path/description/
# TODO: find and fix error

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Que:
    def __init__(self):
        self.data = []

    def enq(self, v):
        self.data.append(v)

    def deq(self):
        v = self.data[0]

        self.data.pop(0)

        return v

    def __len__(self):
        return len(self.data)


def path_len(root, pl = 1):
    if root is None:
        return pl

    if root.left is not None and root.val == root.left.val:
        rl = path_len(root.left, pl + 1)
    else:
        rl = pl

    if root.right is not None and root.val == root.right.val:
        rr = path_len(root.left, pl + 1)
    else:
        rr = pl

    return max(rl, rr)


class Solution:

    def longestUnivaluePath(self, root):
        if root is None:
            return 0

        r1 = 0

        if root.left is not None and root.val == root.left.val:
            r1 += path_len(root.left)

        if root.right is not None and root.val == root.right.val:
            r1 += path_len(root.right)


        lres = self.longestUnivaluePath(root.left)
        rres = self.longestUnivaluePath(root.right)

        res = max(lres, rres, r1)

        return res

    def longestUnivaluePath0(self, root):
        if root is None:
            return 0

        Q = Que()

        Q.enq((root, [0]))

        max_chain_len = 0
        while len(Q):
            node, chain_len = Q.deq()
            max_chain_len = max(max_chain_len, chain_len[0])
            for cn in (node.left, node.right):
                if cn is not None:
                    if cn.val == node.val:
                        chain_len[0] += 1
                        Q.enq((cn, chain_len))
                    else:
                        Q.enq((cn, [0]))

        return max_chain_len


T = TreeNode(5)
T.left = TreeNode(4)
T.right = TreeNode(5)

T.left.left = TreeNode(1)
T.left.right = TreeNode(1)

T.right.left = None
T.right.right = TreeNode(5)



T1 = TreeNode(1)
T1.left = TreeNode(4)
T1.right = TreeNode(5)

T1.left.left = TreeNode(4)
T1.left.right = TreeNode(4)

T1.right.left = None
T1.right.right = TreeNode(5)


T2 = TreeNode(1)

T2.left = TreeNode(2)
T2.right = TreeNode(3)

T2.left.left = TreeNode(2)
T2.left.right = TreeNode(2)
T2.left.right.right = TreeNode(2)

T2.left.left.left = TreeNode(2)

T2.left.left.left.left = TreeNode(1)
T2.left.left.left.right = T


S = Solution()
print(S.longestUnivaluePath(T))
print(S.longestUnivaluePath(T1))
print(S.longestUnivaluePath(T2))