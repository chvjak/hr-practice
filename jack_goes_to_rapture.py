#!/bin/python3

f = open('jack_goes_to_rapture.txt')
def input():
    return f.readline()


# !/bin/python3

import os
import sys
import heapq
from collections import defaultdict


class PQ():
    def __init__(self):
        self.data = []

    def enque(self, k, v):
        heapq.heappush(self.data, (k, v))

    def deque(self):
        return heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)


def dijkstra(adj, weights, s, t, N):
    dist_to = [sys.maxsize] * N

    pq = PQ()

    pq.enque(s, 0)
    dist_to[s] = 0

    while len(pq):
        _, v = pq.deque()
        for vn in adj[v]:
            W = max(0, weights[(v, vn)] - dist_to[v])
            new_dist = dist_to[v] + W
            if dist_to[vn] > new_dist:
                pq.enque(new_dist, vn)
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

        weights[(v_from, v_to)] = weight
        weights[(v_to, v_from)] = weight

    res = dijkstra(adj, weights, 0, g_nodes - 1, g_nodes)
    if res == sys.maxsize:
        print("NO PATH EXISTS")
    else:
        print(res)

