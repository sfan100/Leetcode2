import math
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while True:
            i *= 10
            if i > n:
                break
        res = 0
        print i
        t , k , m = int(math.log10(i)) + 1  , 1 , 1
        while t != m:
            res += (m * 10 ** k)
            m += 1
            k += 1

        res = res - ((i-1-n)*(m-1))
        print res
o = Solution()
o.findNthDigit(11)