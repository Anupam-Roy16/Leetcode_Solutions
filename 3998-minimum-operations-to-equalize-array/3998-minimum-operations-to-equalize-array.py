class Solution:
    def minOperations(self, nums: List[int]) -> int:
        first_num = nums[0]
        for i in range(1,len(nums)):
            if first_num !=nums[i]:
                return 1
        return 0 

        