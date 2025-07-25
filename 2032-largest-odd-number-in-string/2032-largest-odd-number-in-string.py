class Solution:
    def largestOddNumber(self, num: str) -> str:
        size = len(num)
        flag = -1
        for i in range(size-1,-1,-1):
            if int(num[i])%2!=0:
                flag = i
                break 
        if flag ==-1:
            return ""
        else:
            return num[:flag+1]


        