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

        char2str = {}
        str2char = {}
        for i,j in zip(pattern,s.split(' ')):

            if i in char2str and j in str2char:
                if char2str[i] != j or str2char[j] != i :
                    return False
            elif i not in char2str and j not in str2char:
                char2str[i] = j
                str2char[j] = i
            else:
                return False
        return True

# @lc code=end

