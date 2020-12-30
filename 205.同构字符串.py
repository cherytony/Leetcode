#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        return all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))


# @lc code=end
