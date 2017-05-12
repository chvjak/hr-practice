f = open('gridland-metro2.txt')
def input():
    return f.readline()


def is_overlap(l1, r1, l2, r2):
    return l1 <= l2 <= r1


def merge(l1, r1, l2, r2):
    assert(is_overlap(l1, r1, l2, r2))
    return (l1, r2) if r2 > r1 else (l1, r1)

n, m, k = [int(x) for x in input().strip().split()]

tracks = {}
for i in range(k):
    r, c1, c2 = [int(x) for x in input().strip().split()]

    if r not in tracks.keys():
        tracks[r] = []

    tracks[r] += [(c1, c2)]

# O(n*k*k)
for (ti, t) in tracks.items():

    t.sort(key=lambda cc: cc[0])

    merged_tracks = []
    i = 0
    while i < len(t):
        track12 = t[i]
        j = i + 1
        while j < len(t):
            track2 = t[j]
            j += 1

            if is_overlap(track12[0], track12[1], track2[0], track2[1]):
                track12 = merge(track12[0], track12[1], track2[0], track2[1])
            else:
                j -= 1
                break
        i = j
        merged_tracks += [track12]
    tracks[ti] = merged_tracks

lp_cell_count = n * m

deltas = 0
for tr in tracks.values():
    for (c1, c2) in tr:
        deltas += c2 - c1 + 1
lp_cell_count -= deltas

print(lp_cell_count)















