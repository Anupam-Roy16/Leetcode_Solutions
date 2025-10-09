class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_result = 0
        for x in nums:
            xor_result = xor_result ^ x
        if xor_result !=0:
            return len(nums)
        elif nums.count(0) == len(nums):
            return 0
        else:
            return len(nums)-1
        

        