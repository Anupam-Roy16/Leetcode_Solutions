class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            n = i
            count = 0
            while n:
                if n&1:
                    count+=1
                n = n>>1
            if count == k:
                ans += nums[i]
        return ans



        