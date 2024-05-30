class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 0:
            return False
        else:
            for i in range(0,32):
                if 3**i == n:
                    return True
                elif 3>>i > n:
                    break
            return False
                
                    
        