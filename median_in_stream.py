import heapq
class MedianKeeper:
    def __init__(self):
        self.min_pq = []
        self.max_pq = []

    def insert(self, val):
        # insert
        if len(self.min_pq) and val > self.min_pq[0]:
            heapq.heappush(self.min_pq, val)
        else:
            heapq.heappush(self.max_pq, -val)

        while len(self.min_pq) < len(self.max_pq):
            val1 = -heapq.heappop(self.max_pq)
            heapq.heappush(self.min_pq, val1)

        while len(self.min_pq) > len(self.max_pq):
            val1 = heapq.heappop(self.min_pq)
            heapq.heappush(self.max_pq, -val1)



    def get_meadian(self):
        print(self.min_pq)
        print(self.max_pq)
        if len(self.min_pq) == len(self.max_pq):
            return (self.min_pq[0] - self.max_pq[0]) / 2.0
        elif len(self.min_pq) < len(self.max_pq):
            return -self.max_pq[0]
        else:
            return self.min_pq[0]

mk = MedianKeeper()

for i in range(10):
    mk.insert(i)
    print(mk.get_meadian())

