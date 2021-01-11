#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count, condition = 0,None

        for i, key in enumerate(nums):

            if count == 0:
                condition = key

            if key == condition:
                count += 1
            else:
                count -= 1

        return condition


# @lc code=end
