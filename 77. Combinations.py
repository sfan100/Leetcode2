class Solution(object):
    def combine(self, n, k):

        # :type n: int
        # :type k: int
        # :rtype: List[List[int]]
        ret = [ ]

        self.dfs([], 1 , n , k,ret)
        return ret

    def dfs(self, lst, start, n, k,res):
        print(lst)
        if len(lst) == k:
            #res.append(lst)
            res.append(list(lst))
            return
        elif start < n+1:
            lst.append(start)
            self.dfs(lst,start + 1, n , k , res)
            lst.pop()
            self.dfs(lst, start + 1, n, k, res)
o = Solution()
print(o.combine(4,2))