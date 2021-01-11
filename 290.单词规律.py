#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split(' ')):
            return False

        look_up = {}
        for i,j in zip(pattern,s.split(' ')):

            if i in look_up:
                if look_up[i] != j:
                    return False
            else:
                look_up[i] = j
        
        return True

# @lc code=end

