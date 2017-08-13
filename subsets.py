class Solution(object):
    def subsets(self,nums):
        nums.sort()
        res = []
        self.helper(res , [] , nums , 0)
        return res

    def helper(self, res ,path, nums , start):
        res.append(path[:])
        for i in range(start , len(nums)):
            path += [nums[i]]
            self.helper(res,path,nums,i + 1)
            path.pop()

o = Solution()
print o.subsets([1,2,3])