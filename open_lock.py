def neighbors(node, deadends):
    if node in deadends:
        return []

    res = []

    for i, c in enumerate(node):
        new_node = list(node)
        new_node[i] = str((int(c) + 1) % 10)
        s_new_node = ''.join(new_node)
        res.append(s_new_node)

        new_node = list(node)
        new_node[i] = str((int(c) - 1) % 10)
        s_new_node = ''.join(new_node)
        res.append(s_new_node)

    return res


from collections import deque, defaultdict


class Solution(object):
    def openLock(self, deadends, target):
        def enq(node):
            if node in visited:
                print('!')

            Q.append(node)

        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        root = ''.join(['0'] * len(target))

        Q = deque()

        Q.append((root, 0))
        visited = set()
        visited.add(root)


        dd = defaultdict(int)
        while len(Q):
            node, level = Q.popleft()
            dd[node] += 1

            nbrs = neighbors(node, deadends)
            for nn in nbrs:
                if nn == target:
                    return level + 1

                if nn not in visited:
                    #Q.append((nn, level + 1))
                    enq((nn, level + 1))
                    visited.add(nn)

        return -1

S = Solution()

print(S.openLock(["110","112","101","121","011","211","011","211"], "111"))

print(S.openLock(["0201","0101","0102","1212","2002"],"0202"))
print(S.openLock(["27", "29", "18", "38"], "28"))
print(S.openLock(["1110","1112","1101","1121","1011","1211","0111","2111"], "1111"))
print(S.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))

