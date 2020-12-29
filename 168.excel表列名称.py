#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:

        s = string.ascii_uppercase

        r = ''

        while n != 0:

            a = n%26
            if a:
                r = s[a-1]+r
            else:
                r = 'Z'+r
            n = (n-1)//26
        
        return r


# @lc code=end

