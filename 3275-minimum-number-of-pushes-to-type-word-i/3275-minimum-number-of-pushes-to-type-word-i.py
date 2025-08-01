class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            if i<8:
                ans += 1
                print("1")
            elif i>7 and i < 16:
                ans += 2
                print("2")
            elif i>15 and i< 24:
                ans += 3
                print("3")
            else:
                ans+=4
        return ans
        