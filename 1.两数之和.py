#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        look_up = {}

        for i,j in enumerate(nums):
            if target - j in look_up:
                return [look_up.get(target-j),i]           
            else:
                look_up[j] = i
        
        return []
            



        
# @lc code=end

