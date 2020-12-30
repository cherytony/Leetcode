#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        isprime = [True] * n
        rt = 0
        for i in range(2, n):
            if isprime[i]:
                rt += 1
                j = i+i
                while j < n:
                    isprime[j]=False
                    j += i
        return rt

# @lc code=end
