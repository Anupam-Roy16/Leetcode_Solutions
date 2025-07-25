class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        sum_not_included_element = 0 
        nums.sort()
        size = len(nums)
        for i in range(size):
            sum_not_included_element += nums[i]
            if sum_not_included_element >= (total_sum - sum_not_included_element):
                break
        return nums[i:][::-1]

        