#!/bin/python3

f = open('jack_goes_to_rapture.txt')
def input():
    return f.readline()


# !/bin/python3

import os
import sys
import heapq
from collections import defaultdict


class Element:
    def __init__(self, v):
        self.v = v
        self.deleted = False

    def __lt__(self, other):
        return True

    def __repr__(self):
        return "[{}, {}]".format(self.v, self.deleted)


class PQ():
    def __init__(self):
        self.data = []
        self.v2el = {}
        self.count = 0

    def enque(self, k, v):
        e = Element(v)
        heapq.heappush(self.data, (k, e))
        self.v2el[v] = e
        self.count += 1

    def deque(self):
        while len(self.data):
            k, e = heapq.heappop(self.data)
            if not e.deleted:
                v = e.v
                del self.v2el[v]
                break
        else:
            return None, None

        self.count -= 1
        return k, v

    def update_key(self, k, v):
        if v not in self.v2el.keys():
            return

        self.v2el[v].deleted = True
        self.enque(k, v)
        self.count -= 1

    def __len__(self):
        return self.count


def dijkstra(adj, weights, s, t, N):
    dist_to = [sys.maxsize] * N

    pq = PQ()

    for v in range(N):
        pq.enque(sys.maxsize, v)

    pq.update_key(s, 0)
    dist_to[s] = 0

    while len(pq):
        _, v = pq.deque()
        for vn in adj[v]:
            W = max(0, weights[(v, vn)] - dist_to[v])
            new_dist = dist_to[v] + W
            if dist_to[vn] > new_dist:
                pq.update_key(new_dist, vn)
                dist_to[vn] = new_dist

    return dist_to[t]


if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    adj = defaultdict(set)
    weights = {}
    for g_itr in range(g_edges):
        v_from, v_to, weight = map(int, input().split())

        v_from -= 1
        v_to -= 1
        adj[v_from].add(v_to)
        adj[v_to].add(v_from)

        if (v_from, v_to) in weights.keys():
            print('DUPLICATE')
            break
        else:
            weights[(v_from, v_to)] = weight
            weights[(v_to, v_from)] = weight

    res = dijkstra(adj, weights, 0, g_nodes - 1, g_nodes)
    if res == sys.maxsize:
        print("NO PATH EXISTS")
    else:
        print(res)

