class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        for x in s[::-1]:
            if x!=' ':
                return len(x)