import heapq
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.heap = []
        self.capacity = capacity
        self.cnt = 0

    def get(self, key):
        """
        :rtype: int
        """
        self.cnt += 1
        if key not in self.cache:
            return -1
        else:
            for pair in self.heap:
                if pair[1] == key:
                    pair[0] = self.cnt  # just referenced
                    return self.cache[key]

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.cnt += 1
        if len(self.cache) < self.capacity:
            if key not in self.cache:
                heapq.heappush(self.heap, [self.cnt, key])
            else:
                for pair in self.heap:
                    if pair[1] == key:
                        pair[0] = self.cnt  # just referenced
        else:
            if key in self.cache:
                for pair in self.heap:
                    if pair[1] == key:
                        pair[0] = self.cnt
            else:
                self.cache.pop(heapq.heappop(self.heap)[1])
                heapq.heappush(self.heap, [self.cnt, key])

        self.cache[key] = value

cache = LRUCache(2)

cache.set(2,1)
cache.set(1,1)
print cache.get(2)
print cache.heap , cache.cache
cache.set(4,1)
print cache.heap , cache.cache