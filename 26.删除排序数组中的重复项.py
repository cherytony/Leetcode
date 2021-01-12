#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # i, w, l = 0, None, 0
        # if not nums:
        #     return 0

        # while i < len(nums):

        #     if w != nums[i]:
        #         w = nums[i]
        #         l += 1
        #         nums[l-1] = w
        #     else:
        #         i += 1

        # return l

        length = 0

        for i in range(len(nums)):

            if i ==0 or nums[i] != nums[i-1]:
                length +=1
                nums[length -1] = nums[i]
            
        return length

# @lc code=end
