file = open('synchronous-shopping.txt')

def input():
    return file.readline()


import heapq
import sys


def bits_from_array(bits_array):
    res = 0
    for bit in bits_array:
        res |= (1 << (bit - 1))

    return res


class PQ:
    def __init__(self):
        self.data = []

    def enq(self, v):
        heapq.heappush(self.data, v)

    def deq(self):
        return heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)



def dijkstra(adj, fish_in_city, city_count, fish_type_count):
    start_state = (1, fish_in_city[1])
    pq = PQ()
    pq.enq((0, start_state))

    row = [sys.maxsize] * (1 << fish_type_count)
    dist = [row[:] for i in range(city_count + 1)]
    dist[1][fish_in_city[1]] = 0

    while len(pq):
        _, state = pq.deq()

        city, fish_state = state
        for next_city, weight in adj[city]:
            next_fish_state = fish_state | fish_in_city[next_city]

            if dist[next_city][next_fish_state] > dist[city][fish_state] + weight:
                dist[next_city][next_fish_state] = dist[city][fish_state] + weight
                pq.enq((dist[next_city][next_fish_state], (next_city, next_fish_state)))

    return dist


# N, M, K
city_count, road_count, fish_type_count = [int(x) for x in input().strip().split(' ')]

fish_in_city = {}
for c in range(city_count):
    fish_in_city[c + 1] = bits_from_array([int(x) for x in input().strip().split(' ')][1:])

adj = [[] for x in range(city_count + 1)]

for r in range(road_count):
    v_from, v_to, weight = [int(x) for x in input().strip().split(' ')]
    adj[v_from].append((v_to, weight))
    adj[v_to].append((v_from, weight))

final_fish_state = (1 << fish_type_count) - 1
final_state = (city_count, final_fish_state)

dist = dijkstra(adj, fish_in_city, city_count, fish_type_count)
res = sys.maxsize

for ffs1 in range(final_fish_state):
    for ffs2 in range(ffs1 + 1, final_fish_state + 1):
        if ffs1 | ffs2 == final_fish_state:
            if ffs1 != 0:
                d1 = dist[city_count][ffs1]
                d2 = dist[city_count][ffs2]

                res = min(res, max(d1, d2))
            else:
                d2 = dist[city_count][ffs2]

                res = min(res, d2)

print(res)