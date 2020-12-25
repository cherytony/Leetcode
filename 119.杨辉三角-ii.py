#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        result = []

        for i in range(rowIndex+1):
            r = []

            for j in range(i+1):
                if j ==0 or j ==i:

                    r.append(1)
                else:
                    r.append(result[i-1][j-1]+result[i-1][j])
            
            result.append(r)
        
        return result[-1]
# @lc code=end

