class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum ,max_sum = 0, -10000000000
        for num in nums:
            current_sum += num
            if max_sum < current_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum =0
        return max_sum
        
        