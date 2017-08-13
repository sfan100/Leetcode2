class Solution(object):
    def permutation(self,n):
        if n == 1:
            res = []
            res.append(['1'])
            return res
        else:
            origin = self.permutation(n - 1)
            res = []
            for sub in origin:
                sub_res = []
                tem = sub[:]
                i = n - 1
                while i >= 0:
                    tem.insert(i, str(n))
                    sub_res.append(tem)
                    tem = sub[:]
                    i -= 1
                res += sub_res
            return res
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        lst = self.permutation(n)
        lst.sort()
        return ''.join(lst[k -1])