#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        t = []

        push = ['[','{','(']
        pop = [']','}',')']
        dic = {']':'[','}':'{',')':'('}


        if not s:
            return True
        for i in s:
            if i in push:
                t.append(i)
            
            if i in pop:
                if not t:
                    return False
                if t.pop() != dic[i]:
                    return False
        
        return len(t)==0
# @lc code=end

