
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        flag = 1
        carry = a & b
        res = a ^ b
        # if a < 0 and b < 0:
        #     flag = -1
        #     a , b = a*-1 , b*-1
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)



o = Solution()
print(o.getSum(-100,113))