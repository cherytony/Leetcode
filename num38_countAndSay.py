# @Author jerry
# @data 2020年11月24日00:30:52


class Solution:
    def countAndSay(self, n: int) -> str:

        pre = ''
        cur = '1'

        for i in range(1,n):

            pre = cur
            cur = ''

            start =0
            end = 0

            while end < len(pre):
                while end <len(pre) and pre[start] == pre[end]:
                    end += 1

                cur += str(end - start)+pre[start]

                start = end

        return cur
        pass

'''

# 一段高级的代码
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        
        s = self.countAndSay(n-1) + "*"
        res,count = '',1
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count +=1
            else:
                res += str(count) + str(s[i])
                count = 1
        return res
'''

