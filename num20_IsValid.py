class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = '({['
        right = ')}]'

        stack = []
        if not s:
            return True
        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if not stack:
                    return False
                tmp = stack.pop()
                if tmp == '(' and i != ')':
                    return False
                if tmp == '{' and i != '}':
                    return False
                if tmp == '[' and i != ']':
                    return False
        return stack == []

