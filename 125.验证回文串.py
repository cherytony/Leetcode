#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        sc = ''
        for char in s.lower():
            if char.isalnum():
                sc += char
        
        low,high = 0,len(sc)-1
        
        while low<=high:

            if sc[low]==sc[high]:
                low +=1 
                high -=1
            else:
                return False
        
        return True

            


# @lc code=end

