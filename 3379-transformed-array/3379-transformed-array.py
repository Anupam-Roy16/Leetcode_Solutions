class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(nums[i])
            elif nums[i] >0:
                index = (i + nums[i])%len(nums)
                result.append(nums[index])
            else:
                index = i+nums[i]
                if (abs(index)>len(nums)):
                    index = abs(index) % len(nums) 
                    index = -1*index
                result.append(nums[index])
        return result