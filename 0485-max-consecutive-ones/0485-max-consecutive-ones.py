class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = -1
        count ,i= 0, 0
        while i < len(nums):
            if nums[i] ==1:
                count += 1
            else:
                count = 0
            if count > maxx:
                maxx = count
            i += 1
        return maxx
            
                
                
                    
        