#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:

        # if x >=0:
        #     a = int(str(x)[::-1]) 
        #     return a if abs(a)<pow(2,31) else 0
        # else:
        #     a = -1 * int(str(-1 *x)[::-1])
        #     return a if abs(a)<pow(2,31) else 0

        negative = x < 0
        x = abs(x)
        reverse = 0 
        while x:
            reverse = reverse * 10 + x%10
            x = x//10
        
        if reverse> 2**31-1:
            return 0
        
        return -reverse if negative else reverse





# @lc code=end

