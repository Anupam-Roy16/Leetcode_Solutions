class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        'sapce o(n), time o(n),  '
        'it can be solved by two poointer first sort then search '
        
        dictionary = {}
        for i in range(len(nums)):
            if target-nums[i] in dictionary:
                return [i,dictionary[target - nums[i]]]
            else:
                dictionary[nums[i]] = i
        
            
        