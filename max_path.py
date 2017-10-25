f = open('max_path.txt')
def input():
    return f.readline()


def add_edge(G, node_from, node_to, weight):
    if G[node_from] is None:
        G[node_from] = []

    G[node_from].append((node_to, weight))


def DFS_get_depth(G, root, parent=None):
    max_depth = 0
    if parent is None:
        parent = [None] * len(G)
        parent[root] = root

    for n, w in G[root]:
        if parent[n] is None:
            parent[n] = root
            depth = DFS_get_depth(G, n, parent)
            if w + depth > max_depth:
                max_depth = w + depth

    return max_depth

# Non recursive DFS implementation
from collections import deque
def DFS_get_depth_NR(G, root):
    stack = deque()
    stack.append((root, -1, -1))  # and other local vars
    visited = [False]*len(G)
    visited[root] = True

    i = 0
    max_depth = 0
    while len(stack) > 0:
        while i < len(G[root]):
            n, w = G[root][i]
            i += 1

            # go into 'recursion'
            if not visited[n]:
                visited[n] = True
                stack.append((root, i, max_depth)) # and other local vars
                root = n
                i = 0
                max_depth = 0 # res


        # go out of 'recursion'
        max_depth_prev = max_depth
        root, i, max_depth = stack.pop()
        n, w = G[root][i]
        max_depth = max(max_depth, w + max_depth_prev)

    return 0


def BFS(G, root):
    discovered = [root]
    distance = [None] * (len(G))
    distance[root] = 0
    distance[0] = 0


    while len(discovered) > 0:
        n = discovered.pop(0)

        for nn, nw in G[n]:
            if distance[nn] is None:
                distance[nn] = nw + distance[n]

                discovered.append(nn)

    max_distance = max(distance)
    max_distance_node = distance.index(max_distance)
    return max_distance_node, max_distance


T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    if N == 1:
        print(0,0)
        continue
    G = [None] * (N + 1)
    for i in range(N - 1):
        s = input()
        node_from, node_to, weight = [int(x) for x in s.strip().split(' ')]
        add_edge(G, node_from, node_to, weight)
        add_edge(G, node_to, node_from, weight)

    max_distance_node_from1, max_distance_from1 = BFS(G, 1)
    max_distance_node, max_distance = BFS(G, max_distance_node_from1)

    res = max_distance

    if res < 100:
        res1 = 0
    elif res < 1000:
        res1 = 100
    elif res < 10000:
        res1 = 1000
    else:
        res1 = 10000

    print(res1, res)