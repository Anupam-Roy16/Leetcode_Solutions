class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_zero = 0
        for i in range(1,6):
            num_zero +=  int(n / pow( 5, i))
        return num_zero
            
            
        