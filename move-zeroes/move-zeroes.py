class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        loc = -1
        for j in range(len(nums)):
            if nums[j]==0:
                loc = j
                break
        if loc ==-1:
            return nums
        else:
            pos = loc
            for i in range(loc+1,len(nums)):
                if nums[i] != 0:
                    nums[pos] = nums[i]
                    nums[i] = 0
                    pos += 1
            return nums
                