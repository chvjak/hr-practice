#!/bin/python3

import sys

from math import log2


def smallest_bit(number):
    if number == 0:
        return -1

    max_bit = int(log2(number)) + 1

    for i in range(max_bit):
        if number & (1 << i):
            return i

    print('no 1?')
    return -1


def unset_bit(number, bit):
    max_bit = int(log2(number)) + 1
    number &= ~((1 << max_bit) | (1 << bit))

    return number


def set_bit(number, bit):
    number |= 1 << bit

    return number


def neighbor_positions(position):
    position = list(position)
    N_rods = len(position)
    res = []

    # try moving top disk of each rod (i.e smallest bit)
    # to the rest of the rods (i.e nested loop)
    for i in range(N_rods):
        # pick smallest bit on rod i
        sbi = smallest_bit(position[i])

        if sbi == -1:
            continue

        for j in range(N_rods):
            if i != j:
                if position[j] == 0 or sbi < smallest_bit(position[j]):
                    new_position = position[:]
                    new_position[i] = unset_bit(new_position[i], sbi)
                    new_position[j] = set_bit(new_position[j], sbi)
                    res.append(tuple(new_position))

    return res


import heapq


class PQ():
    def __init__(self):
        self.data = []

    def enque(self, k, v):
        heapq.heappush(self.data, (k, v))

    def deque(self):
        return heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)


def highest_bits_match(num1, num2):
    if num2 < num1:
        num2, num1 = num1, num2

    res = 0
    while num1 > 0:
        max_bit1 = int(log2(num1)) + 1
        max_bit2 = int(log2(num2)) + 1

        if max_bit1 != max_bit2:
            return res
        else:
            num1 = unset_bit(num1, max_bit1)
            num2 = unset_bit(num2, max_bit2)

            res += (1 << max_bit1)

    return res


def get_score(next_position, last_position):
    score = 0
    for fp, lp in zip(next_position, last_position):
        score += highest_bits_match(fp, lp)

    return score


def bfs(first_position, last_position):
    # TODO: A* , i.e PQ, with priority for positions 'the closer to target the better = 1st inplace => score + 100, 2nd inplace => score + 100 etc, nothing inplace => score 0'

    q = PQ()
    q.enque(get_score(first_position, last_position), first_position)

    levels = {}
    levels[first_position] = 0

    while len(q):
        _, position = q.deque()

        for next_position in neighbor_positions(position):
            if next_position == last_position:
                return levels[position] + 1

            if next_position not in levels.keys():
                levels[next_position] = levels[position] + 1
                q.enque(get_score(next_position, last_position), next_position)

    print('cant find last pos')
    return -1


N = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

# build graph from  S = (0|1|2|...|2 ^ N, 0, 0) to a
last_position = [0] * 4
for i, rod in enumerate(a):
    last_position[rod - 1] |= 1 << i

first_position = [0] * 4
for i in range(N):
    first_position[0] |= 1 << i

# print(first_position)
# print(last_position)

# print(smallest_bit(10))
# print(set_bit(10, 0))
# print(neighbor_positions(first_position))

print(highest_bits_match(7, 6))

# res = bfs(tuple(first_position), tuple(last_position))
#print(res)