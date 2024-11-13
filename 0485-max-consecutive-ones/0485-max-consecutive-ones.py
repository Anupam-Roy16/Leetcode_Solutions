class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = -1
        i = 0
        while i < len(nums):
            if nums[i] ==1:
                j = i
                count = 0
                while j<len(nums):
                    if nums[j] ==1:
                        count +=1
                        j += 1
                    else:
                        break
                if count > maxx:
                    maxx = count
                i = j+1
            else:
                i += 1
        if maxx ==-1:
            return 0
        return maxx
                    
        