class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        if len(nums) == 1:
            return 1
        else:
            while fast < len(nums):
                if nums[fast] != nums[slow]:
                    nums[slow+1] = nums[fast]
                    slow += 1
                fast += 1
            return slow+1
                
        
        