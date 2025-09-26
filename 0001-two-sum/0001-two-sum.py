class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needy_dict = {}
        for i in range(len(nums)):
            needy_number = target - nums[i]
            if needy_number in needy_dict:
                return [i,needy_dict[needy_number]]
            needy_dict[nums[i]] = i


        