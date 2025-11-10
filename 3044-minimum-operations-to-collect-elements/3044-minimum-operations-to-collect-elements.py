class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        ans = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] <= k:
                s.add(nums[i])
                if len(s) == k:
                    ans = i
                    break
            
        return len(nums)-ans



        