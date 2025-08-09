class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        flag = -1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
                flag = i
                break
        for i in range(flag+1):
            if nums[i] != i+1:
                ans.append(i+1)
                break
        if len(ans) != 2:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] != i+1:
                    ans.append(i+1)
                    break
        return ans


        