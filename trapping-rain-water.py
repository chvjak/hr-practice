import heapq


class Block:
    def __init__(self, h):
        self.h = h
        self.deleted = False

    def __lt__(self, other):
        return self.h < other.h

    def __repr__(self):
        return "[{}, {}]".format(self.h, self.deleted)


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


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        blocks = [None] * N
        rpq = PQ()
        lpq = PQ()
        for x, h in enumerate(height):
            b = Block(h)
            blocks[x] = b
            rpq.enq(b.h, b)

        res = 0  # water volume
        for x in range(N):
            current_block = Block(blocks[x].h)
            lpq.enq(current_block.h, current_block)
            blocks[x].deleted = True  # effects rpq

            lhb, rhb = lpq.get_max(), rpq.get_max()

            if lhb is None:
                lh = 0
            else:
                lh = lhb.h

            if rhb is None:
                rh = 0
            else:
                rh = rhb.h

            if min(lh, rh) - current_block.h > 0:
                res += min(lh, rh) - current_block.h

        return res

S = Solution()

print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1]))