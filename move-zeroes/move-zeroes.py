class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        first find index of first 0  and indicate this position . then after the index find non zero and marked position is initialised by this non zero and increase 1 this position and value set to zero ,and find next non zero. repeated process 
        """
        loc = -1
        for j in range(len(nums)):
            if nums[j]==0:
                loc = j
                break
        if loc ==-1:
            return nums
        else:
            pos = loc
            for i in range(loc+1,len(nums)):
                if nums[i] != 0:
                    nums[pos] = nums[i]
                    nums[i] = 0
                    pos += 1
            return nums
                