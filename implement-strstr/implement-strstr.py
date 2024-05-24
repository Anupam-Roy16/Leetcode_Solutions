class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size1 = len(haystack)
        size2 = len(needle)
        if size2 > size1:
            return -1
        else:
            for i in range(size1-(size2-1)):
                if haystack[i:i+size2] == needle:
                    return i
            return -1