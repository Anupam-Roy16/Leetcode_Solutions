class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        count_one = 0
        length = len(s)
        for i in range(length):
            if s[i] == '1':
                count_one += 1
        
        count_zero = length - count_one  
        count_one -= 1
        str = ''
        for i in range(count_one):
            str += '1'
        for i in range(count_zero):
            str += '0'
        str += '1'
        return str
        
        