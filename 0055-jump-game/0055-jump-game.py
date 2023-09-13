class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=0
        i=0
        while i<=m:
            m=max(m,i+nums[i])
            i+=1
            print(m)
            if m>=len(nums)-1:
                return True
        return False
            
        