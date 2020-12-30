#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        return [f'{t[0]}->{t[-1]}' if len(t :=list(map(itemgetter(1), lst))) > 1 else f'{t[0]}' for _, lst in groupby(enumerate(nums), key=lambda idx_n: idx_n[0]-idx_n[1])]


# @lc code=end
