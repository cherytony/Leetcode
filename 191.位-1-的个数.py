#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:

        s = bin(n)
        count =0

        for i in s[2:]:

            if i == '1':
                count += 1

        
        return count


        
# @lc code=end

