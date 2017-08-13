class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2 or k == 0:
            return 0

        days = len(prices)
        dp = [[0 for i in range(days + 1)] for j in range(min(k + 1, days / 2 + 1))]

        low = prices[0]

        for i in range(1, days + 1):
            if prices[i - 1] < low:
                low = prices[i - 1]
            dp[1][i] = max(dp[1][i - 1], prices[i - 1] - low)


        for i in range(2, len(dp)):
            for j in range(1, len(dp[0])):
                if j / 2 < i:
                    dp[i][j] = dp[i - 1][j]
                else:
                    candidate = 0
                    for k in range(2 * (i - 1) + 1, j):
                        candidate = max(candidate, prices[j - 1] - prices[k - 1] + dp[i - 1][k - 1])
                    dp[i][j] = max(candidate, dp[i - 1][j], dp[i][j - 1])

        print len(dp)
        return dp[-1][-1]
