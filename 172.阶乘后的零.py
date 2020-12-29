#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:

        sum =1

        while n>0:

            sum *= n
            n -= 1
        
        s = str(sum)
        
        count =0
        for i in s[::-1]:

            if i == '0':
                count += 1
            else:
                break
        
        return count




        



# @lc code=end

