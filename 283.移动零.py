#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count, point = 0, 0

        for i in range(len(nums)):

            if nums[i] == 0:
                count += 1
            else:
                nums[point] = nums[i]
                point += 1

        for j in range(point, len(nums)):
            nums[j] = 0
        
        return nums
# @lc code=end
