class Solution:
    def helper(self,minute):
        arr = [60,15,5,1]
        ans = 0
        for i in range(4):
            ans +=(minute//arr[i])
            minute = minute %arr[i]
        return ans



    def convertTime(self, current: str, correct: str) -> int:
        hour1 = int(current[:2])
        hour2 = int(correct[:2])
        minute1 = int(current[3:])
        minute2 = int(correct[3:])

        ans =((hour2 - hour1)*60) - minute1+minute2
        return self.helper(ans)
        



        