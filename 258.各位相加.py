#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:

        while num // 10 !=0 :

            num = reduce(lambda x,y:int(x)+int(y),str(num))
        
        return num
# @lc code=end

