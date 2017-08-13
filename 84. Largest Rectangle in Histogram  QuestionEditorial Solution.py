class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #
        if not heights: return 0
        stack = []  # index of each height in list heights
        area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i if not stack else i - 1 - stack[-1]
                area = max(area, h * width)

            stack.append(i)

        return area
o = Solution()
o.largestRectangleArea([5,6,7,8,3])