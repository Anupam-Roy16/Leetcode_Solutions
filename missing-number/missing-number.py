class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        size *= (size+1)
        size //= 2
        for x in nums:
            size -= x
        return size