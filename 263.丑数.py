#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:

        if num <= 0:
            return False

        nums = [2, 3, 5]
        for i in nums:

            while num % i == 0:
                num //= i

        return num == 1


# @lc code=end
