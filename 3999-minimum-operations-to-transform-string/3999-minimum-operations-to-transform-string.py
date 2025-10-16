class Solution:
    def minOperations(self, s: str) -> int:
        minn = 100000000
        for char in s:
            if char !='a':
                if minn > ord(char):
                    minn = ord(char)
        if minn == 100000000:
            return 0
        return ord('z')-minn+1

        