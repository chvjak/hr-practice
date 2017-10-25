file1 = open("prims_tree.txt")
def input():
    res = file1.readline()
    return res

# should be PQ with keys in prims_dist and values - verteces ids
# this pairs should be in list (heapifieble)
# but when interating through adjacency list should be possible to get (key-dist, vaue-vertex_id) in O(1) =>
# => dictionary {vertex_id => (key-dist, vaue-vertex_id)}
# AND this observation seems to common for all PQs with updatable keys (INCREASE-KEY/DECREASE-KEY)

def get_closest_v(in_tree, prims_dist):
    mi = -1
    md = MAX_INT
    for i, it in enumerate(in_tree):
        if not it:
            if prims_dist[i] < md:
                mi = i
                md = prims_dist[i]

    return mi


def get_prims_tree_weight():
    # prims_parent = [None] * (N + 1) # list of parent nodes

    in_tree = [False] * (N + 1)  # Flags indicating if a vertex in prims tree,
    in_tree[0] = True  # in_tree[0] is dummy for transparent indexing

    prims_dist = [MAX_INT] * (N + 1)  # weight of the edge connecting a vertex to prims tree
    prims_dist[S] = 0  # S - source vertex
    res = 0
    while not all(in_tree):
        v = get_closest_v(in_tree, prims_dist)
        in_tree[v] = True  # how to add edge to prims_tree? what is the parent? how ever weight is known
        res += prims_dist[v]

        for v_to, w in G[v]:
            if not in_tree[v_to]:
                if prims_dist[v_to] > w:
                    prims_dist[v_to] = w

                    # prims_parent[v_to] = v

    return res  # sum(prims_dist[1:]) ? YES!


# Enter your code here. Read input from STDIN. Print output to STDOUT
# vertice count, edges count
N, M = [int(x) for x in input().strip().split(' ')]

G = [None] * (N + 1)  # adjacency list

MAX_INT = 10 ** 20
# read edges
for i in range(M):
    f, t, w = [int(x) for x in input().strip().split(' ')]

    if G[f] is None:
        G[f] = []
    G[f].append((t, w))

    if G[t] is None:
        G[t] = []
    G[t].append((f, w))

S = int(input().strip())

res = get_prims_tree_weight()

print(res)