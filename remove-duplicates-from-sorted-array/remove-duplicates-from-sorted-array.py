class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1
        val = nums[0]
        for i in range(1,len(nums)):
            if val != nums[i]:
                nums[pos] = nums[i]
                pos += 1
                val = nums[i]
        return pos
            
            
        