import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        q,res = [],[1] #the res[0]th ugly number if res[1], using constant space
        if n == 0:
            return 0

        q = [[i,-1] for i in primes]
        heapq.heapify(q)
        print q
        while len(res) < n:
            pair = heapq.heappop(q)
            num , idx = pair[0] , pair[1] + 1
            if num not in res:
                res += [num]
            heapq.heappush(q,[num * primes[idx],idx])
        return res
o = Solution()
o.nthSuperUglyNumber(12,[2,7,13,19])