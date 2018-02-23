import heapq


class Item:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.deleted = False


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.N = capacity
        self.deleted = 0
        self.data = []
        self.key2data = {}
        self.timestamp = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2data.keys():
            return -1

        item = self.key2data[key]
        if item.deleted:
            return -1

        item.deleted = True
        self.deleted += 1
        self.put(item.key, item.val)

        return item.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        old_val = self.get(key)
        if old_val != -1:
            self.key2data[key].val = value
        else:
            item = Item(key, value)
            self.key2data[key] = item
            self.enq(item)

    def enq(self, item):
        heapq.heappush(self.data, (self.timestamp, item))
        self.timestamp += 1

        # consider deleted
        while len(self.data) - self.deleted > self.N:
            __, item = heapq.heappop(self.data)  # consider deleted!
            if item.deleted:
                self.deleted -= 1
            else:
                item.deleted = True


            # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lru = LRUCache(2)
lru.put(2,1)
lru.put(1,1)
lru.put(2,3)
lru.put(4,1)
print(lru.get(1)) # exp: -1
print(lru.get(2)) # exp: 3