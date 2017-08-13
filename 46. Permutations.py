class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, [], res)
        return res

    def helper(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in nums:
            if i not in path:
                path += [i]
                self.helper(nums, path, res)
                path.pop()


o = Solution()
print o.permute([1,2,3,4])