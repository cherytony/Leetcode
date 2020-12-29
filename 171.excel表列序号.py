#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:

        ss = string.ascii_uppercase

        count =1
        look_up = {}
        sum =0
        for chr in ss:
            look_up[chr]=count
            count +=1
        
        for i,ch in enumerate(s[::-1]):


            sum += look_up[ch]*math.pow(26,i)
        
        return int(sum)






# @lc code=end

