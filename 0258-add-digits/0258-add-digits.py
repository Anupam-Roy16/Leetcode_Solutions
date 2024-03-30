class Solution:
    def addDigits(self, num: int) -> int:
        summ = num
        while 1:
            temp = str(summ)
            summ1 = 0
            for x in temp:
                summ1 += int(x)
            if summ1>=0 and summ1<=9:
                return summ1
            summ = summ1