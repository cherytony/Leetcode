class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(0, x):
            if (i * i) <= x:
                i += 1
            else:
                break

        return i - 1


c = Solution()

print(c.mySqrt(8))
