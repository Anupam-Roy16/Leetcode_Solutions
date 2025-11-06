class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans = 0
        i = 0
        while 1:
            if not (n & 1):
                ans +=(1<<i)
            i+=1
            n = n>>1
            if n == 0:
                break
        return ans




        