#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        length = 0 

        for i in range(len(nums)):

            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        
        return length

# @lc code=end

