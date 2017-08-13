class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or sum(height) == 0: return 0

        water, left, right = 0, 0, len(height) - 1
        max_height = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] > max_height:
                    max_height = height[left]
                else:
                    water += max_height - height[left]
                left += 1
            else:
                if height[right] > max_height:
                    max_height = height[right]
                else:
                    water += max_height - height[right]
                right -= 1
        return water


o = Solution()
o.trap([0,1,0,2,1,0,1,3,2,1,2,1])