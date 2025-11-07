class Solution:
    def numberOfSteps(self, num: int) -> int:
        count_1 , count_0 = 0,0
        if num ==0:
            return 0
        while num:
            if (num & 1):
                count_1+=1
            else:
                count_0+=1
            num = num >>1
        ans = (count_1-1)*2 + count_0+1
        return ans


        