#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []

        for i in range(numRows):

            r = []
            for j in range(0,i+1):
                if j==0 or j==i:

                    r.append(1)

                else:
                    r.append(result[i-1][j]+result[i-1][j-1])
        

        return result

# @lc code=end

