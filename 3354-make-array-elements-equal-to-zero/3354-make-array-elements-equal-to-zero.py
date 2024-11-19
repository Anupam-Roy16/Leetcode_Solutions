class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total_sum = 0
        for x in nums:
            total_sum += x
        left_sum = 0
        ans = 0
        for i in range(len(nums)):
            left_sum +=nums[i]
            if nums[i] ==0:
                if abs(left_sum-total_sum+left_sum) == 0:
                    ans +=2
                elif abs(left_sum-total_sum+left_sum) == 1:
                    ans +=1
        return ans