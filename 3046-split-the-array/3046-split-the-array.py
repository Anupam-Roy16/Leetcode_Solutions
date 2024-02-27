class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        max_count = -1
        for val in dictionary.values():
            if val > max_count :
                max_count = val
        if max_count > 2:
            return False
        else:
            return True