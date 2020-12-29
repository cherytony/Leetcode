#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        def helper(n):
            sum =0
            while n:
                n,dig = divmod(n,10)
                sum += dig**2
            return sum

        seen = set()
        seen.add(n)
        
        while n !=1 :

            n = helper(n)

            if n not in seen:
                seen.add(n)
            else:
                return False
        
        return True

            
        

            


# @lc code=end

