import math
class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        minn = 1000000000000
        for i in range(len(nums)):
            if minn > nums[i]:
                minn = nums[i]
        
        flag , count = 0,0
        for i in range(len(nums)):
            if minn == nums[i]:
                count += 1
            if nums[i] % minn!=0:
                flag = 1
        if count ==1:
            return 1
        elif flag == 1:
            return 1
        else:
            return math.ceil(count/2)
        