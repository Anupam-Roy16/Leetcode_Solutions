class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        import math
        val = math.log(n,4)
        
        if val == int(val):
            return True
        else:
            return False
        