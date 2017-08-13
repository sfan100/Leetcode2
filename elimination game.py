class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        lst = [i for i in range(1, n + 1)]
        time, num = 1, 0

        while lst.count(0) != len(lst) - 1:
            if time % 2 == 1:
                for i in range(0, len(lst), 2):
                    lst[i] = 0
            else:

                for i in range(len(lst) - 2, - 1, -2):
                    lst[i] = 0

            time += 1
        return sum(lst)
o = Solution()
print (o.lastRemaining(9))