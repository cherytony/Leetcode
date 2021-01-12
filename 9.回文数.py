#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # if x < 0:
        #     return False
        # reverse = 0
        # temp = x
        # while x:
        #     reverse = reverse*10 + x % 10
        #     x = x//10
        # return reverse == temp


        s = str(x)

        left,right = 0,len(s)-1

        while left<right:
            if s[left] != s[right]:
                return False
            
            left +=1
            right -=1
        
        return True



# @lc code=end
