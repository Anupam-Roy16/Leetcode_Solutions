class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            flag = 0
            for i in range(1,1025):
                if i|(i+1) == x:
                    flag = 1
                    ans.append(i)
                    break
            if flag == 0:
                ans.append(-1)
        return ans