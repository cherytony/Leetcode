#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # result = []

        # for i in range(len(prices):
        #     max =0
        #     for j in range(i+1,len(prices)):
        #         t= prices[j]-prices[i]
        #         if t>max:
        #             max = t
        #     result.append(max)

        # return max(result)

        # 
        
        min_price = int(1e9)
        max_result = 0

        for price in prices:

            max_result = max(max_result,price-min_price)
            min_price = min(min_price,price)

        return max_result


                    
# @lc code=end

