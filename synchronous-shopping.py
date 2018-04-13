file = open('synchronous-shopping.txt')

def input():
    return file.readline()


from collections import defaultdict
from collections import deque
import heapq
import sys


class PQ:
    def __init__(self):
        self.data = []

    def enq(self, v):
        heapq.heappush(self.data, v)

    def deq(self):
        return heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)


def bits_from_array(bits_array):
    res = 0
    for bit in bits_array:
        res |= (1 << bit)

    return res


def dijkstra(adj, weights, s, t):
    pq = PQ()
    pq.enq((0, s))
    dist = {}
    dist[s] = 0

    path_to = {}

    while len(pq):
        _, v = pq.deq()
        for u in adj[v]:
            if u not in dist.keys():
                dist[u] = sys.maxsize

            if dist[u] > dist[v] + weights[(v, u)]:
                dist[u] = dist[v] + weights[(v, u)]
                path_to[u] = v
                pq.enq((dist[u], u))

    n = t
    path = []
    while n != s:
        path.append(n)
        n = path_to[n]
    path.append(s)

    # print(path)
    return dist[t]


# N, M, K
city_count, road_count, fish_type_count = [int(x) for x in input().strip().split(' ')]

fish_in_city = {}
for c in range(city_count):
    fish_in_city[c + 1] = bits_from_array([int(x) for x in input().strip().split(' ')][1:])

adj = defaultdict(set)
weights = {}
for r in range(road_count):
    v_from, v_to, weight = [int(x) for x in input().strip().split(' ')]
    adj[v_from].add(v_to)
    adj[v_to].add(v_from)
    weights[(v_from, v_to)] = weight
    weights[(v_to, v_from)] = weight

# generate states as combination (i.e cross product) of neighbor states of cat1 and cat2 i.e BFS
# CONCERN: too complex - O(E^2V^2)
cat1_pos = 1
cat2_pos = 1
q = deque()
start_pos = ((1, 1), fish_in_city[1])
target_pos = ((city_count, city_count), bits_from_array(range(1, fish_type_count + 1)))

q.append(start_pos)
visited = set()
visited.add(start_pos)

new_adj = defaultdict(set)
new_weights = {}

while len(q):
    pos = q.popleft()
    (cat1_pos, cat2_pos), fish_pos = pos

    for c1_next in adj[cat1_pos] | set([cat1_pos]):
        if cat1_pos != c1_next:
            c1_dist = weights[(cat1_pos, c1_next)]
        else:
            c1_dist = 0

        for c2_next in adj[cat2_pos] | set([cat2_pos]):
            if cat2_pos != c2_next:
                c2_dist = weights[(cat2_pos, c2_next)]
            else:
                c2_dist = 0

            if c1_dist == c2_dist == 0:
                continue

            new_fish_pos = fish_pos | fish_in_city[c1_next] | fish_in_city[c2_next]
            if c1_next > c2_next:
                new_pos = ((c2_next, c1_next), new_fish_pos)
            else:
                new_pos = ((c1_next, c2_next), new_fish_pos)

            new_adj[pos].add(new_pos)
            new_weights[(pos, new_pos)] = max(c1_dist, c2_dist)

            if new_pos in visited or new_pos == target_pos:
                continue

            visited.add(new_pos)
            q.append(new_pos)

# print(new_adj)
# print(new_weights)

res = dijkstra(new_adj, new_weights, start_pos, target_pos)

print(res)
