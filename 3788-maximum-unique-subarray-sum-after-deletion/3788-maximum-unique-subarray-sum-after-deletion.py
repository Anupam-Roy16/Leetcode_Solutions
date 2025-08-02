class Solution:
    def maxSum(self, nums: List[int]) -> int:
        temp_set = set()
        for x in nums:
            if x>=0:
                temp_set.add(x)
        if len(temp_set) == 0:
            nums.sort()
            return nums[-1]
        else:
            temp_list = list(temp_set)
            return sum(temp_list)