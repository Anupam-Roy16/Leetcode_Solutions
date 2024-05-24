class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            x *= -1
            flag = 1
        s = str(x)
        s = s[::-1]
        s = int(s)
        if flag == 1:
            s *= -1
        if s < (-1*(2**31)) or s > (2**31):
            return 0
        else:
            return s
        