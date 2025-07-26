class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        frequency_dict = {}
        for x in nums:
            if x!=0:
                if x not in frequency_dict:
                    frequency_dict[x] =1
                else:
                    frequency_dict[x] +=1
        return len(frequency_dict)
        