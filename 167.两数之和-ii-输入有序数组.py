#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        look_up = {}

        for i,num in enumerate(numbers):

            if target-num not in look_up:
                look_up[num]=i
            else:
                return look_up[target-num]+1,i+1
# @lc code=end

