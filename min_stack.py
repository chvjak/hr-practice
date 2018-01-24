import heapq


class MinPQI:
    def __init__(self):
        self.heap = []
        self.keys_to_obj = {}

    def enq(self, val):
        obj = [val, False]
        self.keys_to_obj[val] = obj
        heapq.heappush(self.heap, obj)

    def deq(self):
        while not self.is_empty():
            key, deleted = heapq.heappop(self.heap)
            if not deleted:
                return key
        else:
            return None

    def getMin(self):
        if not self.is_empty():
            v = self.deq()
            self.enq(v)

            return v
        else:
            return -1


    def remove(self, val):
        self.keys_to_obj[val][1] = True  # deleted = True

    def is_empty(self):
        return len(self.heap) == 0


class MinStack:
    def __init__(self):
        self.mpq = MinPQI()
        self.data = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.data.append(x)
        self.mpq.enq(x)

    def is_empty(self):
        return len(self.data) == 0

    # @return nothing
    def pop(self):
        if not self.is_empty():
            val = self.data.pop()
            self.mpq.remove(val)

    # @return an integer
    def top(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if not self.is_empty():
            return self.mpq.getMin()
        else:
            return -1



ms = MinStack()

s = "P10 P9 g P8 g P7 g P6 g p g p g p g p g p g"
commands = s.split(' ')

for c in commands:
    if c == 'p':
        ms.pop()
    elif c == 'g':
        print(ms.getMin())
    else:
        #PX
        v = int(c[1:])
        ms.push(v)



