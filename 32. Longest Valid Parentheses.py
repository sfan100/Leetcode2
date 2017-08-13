from heapq import  heapify

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(['(', i])
            else:
                length = 0
                if stack and stack[-1] == '(':
                    stack.pop()
                    if stack:
                        length = i - stack[-1][1]
                    else:
                        length = i + 1

                    res = max(res, length)

                else:
                    stack.append([')', i])

        return res

o = Solution()
o.longestValidParentheses('()')



