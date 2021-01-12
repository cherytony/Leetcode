#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:

        double = {'IV': 4,'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        single = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        sum = 0
        i = 0

        while i < len(s):
            if i < len(s)-1 and s[i: i+2] in double:
                sum += double[s[i:i+2]]
                i += 2
            else:
                sum += single[s[i]]
                i += 1
        return sum


# @lc code=end
