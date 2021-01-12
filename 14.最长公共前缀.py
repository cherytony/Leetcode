#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        # if not strs:
        #     return ""

        # strs.sort()

        # first, last = strs[0], strs[-1]

        # i = 0
        # while i < len(first) and i < len(last) and first[i] == last[i]:
        #     i += 1

        # return first[:i]


        '''
        first try.
        '''
        if not strs:
            return ""

        if len(strs) ==1:
            return strs[0]

        targe = strs[0]
        index =0
        retrip = ""
        while index < len(targe):

            for i in range(1,len(strs)):
                if not strs[i]:
                    return ""

                if  index > len(strs[i])-1:
                    return retrip

                if targe[index] != strs[i][index]:
                    return retrip
            index += 1
            retrip = targe[:index]

# @lc code=end

