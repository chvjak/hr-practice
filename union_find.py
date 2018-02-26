class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.cc_count = N


    def find(self, a):
        if self.parent[a] != a:
            return self.find(self.parent[a])
        return a


    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a != parent_b:
            if self.rank[parent_a] > self.rank[parent_b]:
                self.parent[parent_b] = parent_a
            elif self.rank[parent_a] < self.rank[parent_b]:
                self.parent[parent_a] = parent_b
            else:
                self.parent[parent_a] = parent_b
                self.rank[parent_b] += 1

            self.cc_count -= 1


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        N = len(M)
        uf = UnionFind(N)

        for i in range(N - 1):
            for j in range(i + 1, N):
                if M[i][j] == 1:
                    #print(i,j)
                    uf.union(i, j)

        return uf.cc_count



S = Solution()
print(S.findCircleNum([[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,0,1,0,1,0,0,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,1,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,1,1,0,1,1,0,0],[0,0,0,0,0,0,0,0,1,0,1,1,0,0,0],[0,0,1,0,1,1,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],[0,1,0,1,0,0,0,0,1,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,1,0,1]]))
