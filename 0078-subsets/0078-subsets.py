class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1<<n):
            v = []
            for j in range(n):
                if (i &(1<<j)):
                    v.append(nums[j])
            ans.append(v)
        return ans
                    
        
        