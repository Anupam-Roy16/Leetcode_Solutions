class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        val = 0
        for i in range( len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j]) <= min(nums[i],nums[j]):
                    temp = nums[i] ^ nums[j]
                    if temp>val:
                        val = temp
        return val;
                
        