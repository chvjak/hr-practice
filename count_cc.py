from collections import defaultdict


class Graph:
    def __init__(self, N):
        self.N = N
        self.adj = defaultdict(set)

    def add(self, from1, to1):
        self.adj[from1].add(to1)
        self.adj[to1].add(from1)


def count_cc(G):
    visited = set()

    def dfs(root):
        visited.add(root)

        for nn in G.adj[root]:
            if nn not in visited:
                dfs(nn)

    cc_count = 0
    prev_len_visited = 0

    for i in G.adj.keys():
        dfs(i)

        if len(visited) > prev_len_visited:
            cc_count += 1

        prev_len_visited = len(visited)

    return cc_count


def to_id(grid, r, c):
    R = len(grid)
    C = len(grid[0])

    return C * r + c


def get_neighbors(grid, r, c):
    R = len(grid)
    C = len(grid[0])

    neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

    res = []
    for r, c in neighbors:
        if 0 <= r < R and 0 <= c < C:
            res.append((r, c))

    return res


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        """
        # Count connected components
        R = len(grid)
        if R == 0:
            return 0
        C = len(grid[0])
        G = Graph(R * C)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == '1':
                    id1 = to_id(grid, r, c)
                    G.add(id1, id1)
                    neighbors = get_neighbors(grid, r, c)
                    for nr, nc in neighbors:
                        if grid[nr][nc] == '1':
                            id2 = to_id(grid, nr, nc)
                            G.add(id1, id2)

        res = count_cc(G)

        return res


S = Solution()
print(S.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

print(S.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(S.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
