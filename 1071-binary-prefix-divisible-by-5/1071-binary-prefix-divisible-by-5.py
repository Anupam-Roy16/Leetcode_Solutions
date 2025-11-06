class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        ans = []
        for i in range(len(nums)):
            if nums[i] ==0:
                num*=2
            else:
                num*=2
                num+=1
            if num %5 ==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        

        