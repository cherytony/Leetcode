"""
@Author Jerry
@date 2020年11月24日23:47:34
"""


class Solution:
    def maxSubArray(self, nums) -> int:

        max_sum = nums[0]
        pre = 0

        for i in range(0, len(nums)):

            if i == 0:
                cur = nums[0]
            else:
                cur = max(pre + nums[i], nums[i])

            if max_sum < cur:
                max_sum = cur

            pre = cur

        return max_sum
