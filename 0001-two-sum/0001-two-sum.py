class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            if target-nums[i] in dictionary:
                return [i,dictionary[target - nums[i]]]
            else:
                dictionary[nums[i]] = i
        
            
        