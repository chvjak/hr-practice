from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj = defaultdict(set)

    def add(self, from_v, to_v):
        self.adj[from_v].add(to_v)
        self.adj[to_v].add(from_v)


def dfs_loop(G, root, parents):
    for v in G.adj[root]:
        if parents[root] != v:
            if parents[v] is not None:
                parents[v] = root
                return root
            else:
                parents[v] = root
                res = dfs_loop(G, v, parents)

                if res is not None:
                    return res

    return None


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        G = Graph()
        for from_v, to_v in edges:
            G.add(from_v, to_v)

        N = len(G.adj)
        parents = [None] * (N + 1)
        parents[1] = 1
        loop_start = dfs_loop(G, 1, parents)

        print(loop_start, parents)

        loop_edge_ixs = []
        cur_vertex = loop_start
        while True:
            prev_vertex = cur_vertex
            cur_vertex = parents[cur_vertex]
            edge = [min(prev_vertex, cur_vertex), max(prev_vertex, cur_vertex)]

            loop_edge_ixs.append(edges.index(edge))

            if cur_vertex == loop_start:
                break

        loop_edge_ixs.sort(reverse=True)

        return edges[loop_edge_ixs[0]]


S = Solution()
print(S.findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))
print(S.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]]))

