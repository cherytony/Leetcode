#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):

        size = len(prices)

        dp0 = 0
        dp1 = -prices[0]

        for i in range(1, size):
            tmp = dp0
            dp0 = max(dp0, dp1+prices[i])
            dp1 = max(dp1, tmp-prices[i])

        return dp0


# @lc code=end
