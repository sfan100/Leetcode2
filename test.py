from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        target = defaultdict(list)
        tickets.sort(key=lambda a: a[1], reverse=True)

        for a, b in tickets:
            target[a] += [b]

        stack, res = ['JFK'], []

        while stack:
            if not target[stack[-1]]:
                res += [stack.pop()]
            else:
                while target[stack[-1]]:
                    stack += [target[stack[-1]].pop()]
        return res[::-1]

o = Solution()
print o.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])