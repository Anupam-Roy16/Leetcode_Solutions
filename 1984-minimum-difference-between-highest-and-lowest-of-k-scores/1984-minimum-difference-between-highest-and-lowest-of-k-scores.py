class Solution:
    #first sort . then iterate to find minimum diffrence between two number at k distance  
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = (k-1)
        min_diff = 100000000000
        for j in range(len(nums)):
            if min_diff > nums[i] - nums[j]:
                min_diff = nums[i] - nums[j]
            i += 1
            if i == len(nums):
                break
        return min_diff