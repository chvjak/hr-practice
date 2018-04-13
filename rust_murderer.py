#!/bin/python3

f = open('rust_murderer.txt')
def input():
    return  f.readline()



import os
import sys

from collections import deque


def dfs(s, adj_mtx):
    N = len(adj_mtx)
    q = deque()
    q.append(s)
    levels = [None] * N
    levels[s] = 0
    not_discovered = set(range(N))
    not_discovered.remove(s)

    while q:
        v = q.popleft()

        adj = [i for i in not_discovered if i not in adj_mtx[v]]
        for vn in adj:
            if levels[vn] is None:
                levels[vn] = levels[v] + 1
                q.append(vn)
                not_discovered.remove(vn)

    return levels[:s] + levels[s + 1:]


def rustMurderer(n, s, roads):
    #
    # Write your code here.
    #
    adj_mtx = {i:set() for i in range(n)}
    s -= 1

    for from_r, to_r in roads:
        from_r -= 1
        to_r -= 1
        adj_mtx[from_r].add(to_r)
        adj_mtx[to_r].add(from_r)

    # print(roads)
    # print(adj_mtx)

    res = dfs(s, adj_mtx)

    return res


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = rustMurderer(n, s, roads)

        print(' '.join(map(str, result)))

