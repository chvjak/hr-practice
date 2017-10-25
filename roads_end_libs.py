file1 = open("roads_and_libs2.txt")
def input():
    res = file1.readline()
    return res


def get_connected_components():
    def DFS(s, discovered):
        discovered.add(s)
        for v in G[s]:
            if v not in discovered:
                DFS(v, discovered)

    discovered = set()
    res = []
    for v in range(1, V + 1):
        if v not in discovered:
            cc = set()
            DFS(v, cc)
            res.append(cc)
            discovered.update(cc)

    return res


def get_cc_cost(cc):
    def BFS_LIM_DEPTH(root):
        edge_count = 0
        levels = [-1] * (V + 1)
        levels[root] = 0
        discovered = [root]
        visited[root] = True

        while len(discovered) > 0:
            v = discovered.pop(0)
            for v1 in G[v]:
                if not visited[v1] and (levels[v] + 1) * CR <= CL:
                    discovered.append(v1)
                    visited[v1] = True
                    levels[v1] = levels[v] + 1
                    edge_count += 1

        return edge_count

    G1 = [(len(G[v]), v) for v in cc]
    G1.sort(key=lambda x: x[0], reverse=True)

    visited = [False] * (V + 1)
    res = 0
    for sink, max_cv in G1:
        if not visited[max_cv]:
            res += CL  # place library in most connected vertex
            res += CR * BFS_LIM_DEPTH(max_cv)

    return res


def get_min_cost():
    CCS = get_connected_components()

    res = 0
    # loop through all 'aglomerations ' AKA connected components
    for cc in CCS:
        res += get_cc_cost(cc)

    return res


Q = int(input().strip())

for q in range(Q):
    V, E, CL, CR = [int(x) for x in input().strip().split(' ')]

    G = [[] for x in range(V + 1)]

    # read roads-edges
    for i in range(E):
        v_from, v_to = [int(x) for x in input().strip().split(' ')]

        G[v_from].append(v_to)
        G[v_to].append(v_from)

    res = get_min_cost()

    print(res)
