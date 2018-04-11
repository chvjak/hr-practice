#!/bin/python3

f = open('jack_goes_to_rapture.txt')
def input():
    return f.readline()


import os
import sys
import heapq
from collections import defaultdict

import networkx as nx
import matplotlib.pyplot as plt

class PQ():
    def __init__(self):
        self.data = []

    def enque(self, k, v):
        heapq.heappush(self.data, (k, v))

    def deque(self):
        return heapq.heappop(self.data)

    def update_key(self, k, v):
        ix = 0
        for _, v1 in self.data:
            if v1 == v:
                break
            else:
                ix += 1

        if ix == len(self.data):
            return

        self.data[ix] = (k, v)

        heapq.heapify(self.data)  # O(N)

    def __len__(self):
        return len(self.data)


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
    G = nx.Graph()
    G.add_nodes_from(range(g_nodes))

    for g_itr in range(g_edges):
        v_from, v_to, weight = map(int, input().split())

        v_from -= 1
        v_to -= 1
        adj[v_from].add(v_to)
        weights[(v_from, v_to)] = weight

        G.add_edge(v_from, v_to, weight=weight)

    #elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 1000]
    #esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 1000]

    #pos = nx.spring_layout(G)  # positions for all nodes

    # edges
    #nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    #nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color='b', style='dashed')

    #nx.draw(G, with_labels=True, pos=pos)
    nx.draw_spring(G, with_labels=True, k=1, iterations=1)
    plt.show()

    res = dijkstra(adj, weights, 0, g_nodes - 1, g_nodes)

    print(res)

