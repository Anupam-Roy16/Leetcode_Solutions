class Solution:
    #by slicing the rotated part
    def check(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                flag = 1
                break
        if flag == 0:
            return True
        nums = nums[i:len(nums)] + nums[0:i]
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True