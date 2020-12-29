#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        from collections import Counter

        look_up = Counter(nums)

        for k,v in look_up.items():
            if v >= len(nums)/2:
                return k


# @lc code=end

