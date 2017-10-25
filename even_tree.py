f1 = open('even_tree.txt')
def input():
    return f1.readline()

def count_max_remove(root):
    res = 0
    nc_sum = 1
    for v in G[root]:
        rc, nc = count_max_remove(v)

        res += rc
        if nc % 2 == 0:
            res += 1
        nc_sum += nc

        # if ALL_EVEN(nc_list):
        # if ROOT _IS_ part of connected component i.e connected ABOVE
        # could be removed count(G[root])
        # elif 1_ODD(nc_list)
        # could be removed count(G[root]) - 1
    # else more than 1 odd => "each odd needs a pair" + "root" = if number of ODD CC + 1 is even than edge to ROOT could be removed

    return res, nc_sum


V, E = [int(x) for x in input().strip().split(' ')]

G = [None] * (V + 1)  # +1 to not count node 0
for i in range(E):
    t, f = [int(x) for x in input().strip().split(' ')]

    if G[f] is None:
        G[f] = []
    if G[t] is None:
        G[t] = []

    G[f].append(t)
    # G[t].append(f)

res, sink = count_max_remove(1)

print(res)