#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:

        def helper(n):
            for i in range(2, n+1):
                if n % i == 0:
                    return False
            return True

        if n == 0 or n == 1:
            return 0
        else:
            count = 0
            for i in range(2, n+1):
                if helper(i):
                    count += 1
        return count
# @lc code=end
