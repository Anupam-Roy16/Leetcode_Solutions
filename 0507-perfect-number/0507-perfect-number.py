class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        if num == 1:
            return False
        for x in range(1,int(num**0.5)+1):
            if num % x == 0:
                sum+= x
                if x!=1:
                    sum += (num//x)
        if sum == num:
            return True
        else:
            return False
        