import heapq


class Building:
    def __init__(self, l, r, h):
        self.l = l
        self.r = r
        self.h = h
        self.deleted = False

    def __lt__(self, other):
        return self.h < other.h


class PQ:
    def __init__(self):
        self.data = []

    def enq(self, key, val):
        # heap is minheap, we need maxheap
        heapq.heappush(self.data, (-key, val))

    def deq(self):
        while len(self.data):
            key, val = heapq.heappop(self.data)
            if not val.deleted:
                return val

        return None

    def get_max(self):
        val = self.deq()
        if val is not None:
            self.enq(val.h, val)

        return val


from collections import defaultdict


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        pq = PQ()
        starts_map = defaultdict(list)
        ends_map = defaultdict(list)

        min_l = 10000
        max_r = 0

        nums = set()
        for l, r, h in buildings:
            b = Building(l, r, h)
            starts_map[l].append(b)
            ends_map[r].append(b)
            nums.add(l)
            nums.add(r)

        res = []
        prev_max = 0
        nums_list = list(nums)
        nums_list.sort()
        for i in nums_list:

            for b in starts_map[i]:
                pq.enq(b.h, b)

            for b in ends_map[i]:
                b.deleted = True

            max_building = pq.get_max()
            if max_building is not None:
                max_height = max_building.h
            else:
                max_height = 0

            if max_height != prev_max:
                res.append((i, max_height))
                prev_max = max_height

        return res


S = Solution()
print(S.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))