import random
from collections import deque
class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__pool, self.__pos = [], {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.__pool:
            self.__pool += [val]
            self.__pos[val] = deque()
            self.__pos[val] += [len(self.__pool) - 1]

            return True
        else:
            self.__pool += [val]
            self.__pos[val] += [len(self.__pool) - 1]
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val in self.__pool:
            if len(self.__pool) == 1:
                self.__pool.pop()
                self.__pos = {}
            else:
                idx, last = self.__pos[val][-1], self.__pool[-1]
                if last == val:
                    self.__pool.pop()
                    self.__pos[last].pop()
                else:
                    self.__pool[-1], self.__pool[idx] = self.__pool[idx], self.__pool[-1]
                    self.__pos[val].pop()
                    self.__pool.pop()
                    self.__pos[last].pop()
                    if not self.__pos[last] or idx < self.__pos[last][-1] :
                        self.__pos[last].appendleft(idx)
                    else:
                        self.__pos[last].append(idx)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        rand = random.randrange(0, len(self.__pool))
        print self.__pool[rand]

    def p(self):
        print self.__pool , self.__pos

r = RandomizedCollection()
# r.insert(9)
# r.insert(9)
r.insert(1)
r.insert(1)
r.insert(2)
r.p()
r.getRandom()
r.remove(1)

# r.remove(2)
# r.remove(1)
# r.remove(1)
#
# r.p()
