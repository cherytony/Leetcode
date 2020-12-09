class Solution:
    # 方案一
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        length = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+length] == needle:
                return i

        return -1

    # 方案二
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)