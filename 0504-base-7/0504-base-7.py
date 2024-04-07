class Solution:
    def convertToBase7(self, num: int) -> str:
        neg = 0
        if num<0:
            num *= -1
            neg = 1
        elif num == 0:
            return "0"
        s = ""
        while num !=0:
            rem = num % 7
            s += str(rem)
            num //= 7
        if neg == 1:
            return "-"+s[::-1]
        else:
            return s[::-1]
            
        
        
        