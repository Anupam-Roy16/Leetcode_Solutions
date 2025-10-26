class Solution:
    def findComplement(self, num: int) -> int:
        n = 1
        flag = 0
        for i in range(32):
           
            if n & num:
                flag = i
            n = n << 1
        print(flag)
        n = 1
        for i in range(flag+1):
            
            num = n ^ num
            n = n <<1
        return num






        