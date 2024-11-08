class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = True
        if dividend < 0 and divisor < 0:
            sign = True
        elif dividend <0 or divisor <0:
            sign = False
        divisor = abs(divisor)
        dividend = abs(dividend)
        ans = 0
        while 1:
            i = 0
            if dividend < divisor:
                break
            while (dividend >= divisor << i):
                i+=1
            ans += (1<<(i-1))
            #print(ans , i,divisor<<i)
            dividend -= (divisor<<(i-1))
            #print(dividend)
        #print(ans)
        if sign:
            if ans > ((1 << 31) -1):
                return (1<<31) -1
            else:
                return ans
        else:
            if (-1*ans) < (-1)*(1<<31):
                return -1*(1 << 31)
            else:
                return (-1)*ans
        