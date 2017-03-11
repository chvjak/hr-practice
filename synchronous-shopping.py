file = open('synchronous-shopping.txt')

def input():
    return file.readline()

MAX_SIZE = 10 ** 20
def flloyd_warshall(G):
    N = len(G)

    fwd = [row[:] for row in G]  # Floyd-Warshall distance

    for i in range(N):
        fwd[i][i] = 0

    for k in range(N):
        for i in range(N - 1):
            for j in range(i + 1, N):
                fwd[j][i] = fwd[i][j] = min(fwd[i][j], fwd[i][k] + fwd[k][j])

    return fwd


def get_direction_to_fishtype(fw_distances, fish_types_by_mall):
    N = len(fw_distances)
    K = len(fish_types_by_mall)

    tr = [MAX_SIZE] * K
    fw_ft = [tr[:] for i in range(N)]
    for i in range(N):
        for k in range(K):
            min_fw = MAX_SIZE
            min_j = None
            for j in range(N):
                if k in fish_types_by_mall[j]:
                    if fw_distances[i][j] < min_fw:
                        min_fw = fw_distances[i][j]
                        min_j = j

            fw_ft[i][k] = min_j

    return fw_ft

from itertools import permutations
def get_min_all_permutations_distance(fish_types_set):
    all_permutations = permutations(fish_types_set)

    min1 = MAX_SIZE
    for p in all_permutations:
        current_pos = 0
        distance = 0
        for ft in p:
            for m in malls_by_fish_type[ft]:
                next_pos = m
                distance += fw_distances[current_pos][next_pos]
                current_pos = next_pos

        # add distance to N <- THIS IS AN ERROR. 
        # Should check ALL (not just closest) possible malls to find shortest root to N 
        distance += fw_distances[current_pos][N - 1]

        min1 = min(min1, distance)

    return min1


from itertools import combinations
def get_all_subset_pairs(elements):
    elements_set = set(elements)
    all_subset_pairs = []
    N = len(elements)
    for i in range(1, N):
        for ss in combinations(elements, i):

            all_subset_pairs += [(elements_set.difference(set(ss)), set(ss))]

    return all_subset_pairs


N, M, K = [int(x) for x in input().strip().split()]

fish_types_by_mall = [None] * N

for i in range(N):
    n_fish_types_by_mall = [int(x) for x in input().strip().split()]
    fish_types_by_mall_i = n_fish_types_by_mall[1:] # 1st elem is length, drop it

    fish_types_by_mall[i] = [x - 1 for x in fish_types_by_mall_i]

malls_by_fish_type = [None] * K
for i in range(N):
    fts = fish_types_by_mall[i]
    for ft in fts:
        if malls_by_fish_type[ft] is None:
            malls_by_fish_type[ft] = []
        malls_by_fish_type[ft] += [i]


row = [MAX_SIZE] * N
G = [row[:] for i in range(N)]

for j in range(M):
    f, t, w = [int(x) for x in input().strip().split()]
    f -= 1
    t -= 1
    G[f][t] = w
    G[t][f] = w

fw_distances = flloyd_warshall(G)
direction_to_fishtype = get_direction_to_fishtype(fw_distances, fish_types_by_mall)

fish_1N = set(fish_types_by_mall[0]).union(set(fish_types_by_mall[-1]))   # fish availble in 1st and last malls => should not be bought on the way
fish_to_buy = set(range(K)).difference(fish_1N)
ft_ss = get_all_subset_pairs(fish_to_buy)  # All 2^K subsets of fish types not in 1st or Nth mall

min_max = MAX_SIZE
for (ss1, ss2) in ft_ss:
    md1 = get_min_all_permutations_distance(ss1)
    md2 = get_min_all_permutations_distance(ss2)

    min_max = min(min_max, max(md1,md2))

print(min_max)