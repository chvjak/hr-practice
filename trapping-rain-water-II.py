from collections import deque
import sys


class Queue:
    def __init__(self):
        self.data = deque()

    def enq(self, v):
        self.data.append(v)

    def deq(self):
        return self.data.popleft()

    def __len__(self):
        return len(self.data)


def neighbors(p, R, C):
    (r, c) = p
    all_neightbors = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
    return ((r, c) for r, c in all_neightbors if 0 <= r < R and 0 <= c < C)


class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        R = len(heightMap)
        if R == 0:
            return 0

        C = len(heightMap[0])

        if C == 0:
            return 0

        res = 0
        waterLevel = [[sys.maxsize] * C for r in range(R)]

        Q = Queue()

        # BFS::QUEUE is primed with all 'outer ring' or 'border'
        # also water level on border is 0
        for r in (0, R - 1):
            for c in range(C):
                Q.enq((r, c))
                waterLevel[r][c] = 0

        for r in range(R):
            for c in (0, C - 1):
                Q.enq((r, c))
                waterLevel[r][c] = 0

        while len(Q):
            r, c = Q.deq()

            for r_next, c_next in neighbors((r, c), R, C):
                # potential water in (r_next, c_next) is weather equal to water level in it's curretly processed neighbor (r, c)
                # if r,c is SEA BED,
                # or equal to heightMap[r][c]
                # if  r,c is WALL
                # each neighbor updates current cell
                # if current cell was updated all it's neighbors should be updated (instead of BFS::VISITED)
                new_water_level = max(waterLevel[r][c], heightMap[r][c])

                if waterLevel[r_next][c_next] > new_water_level:
                    waterLevel[r_next][c_next] = new_water_level

                    Q.enq((r_next, c_next))

        res = 0
        for r in range(R):
            for c in range(C):
                res += max(0, waterLevel[r][c] - heightMap[r][c])
                if max(0, waterLevel[r][c] - heightMap[r][c]) > 0:
                    print(r, c, waterLevel[r][c] - heightMap[r][c])

        return res
