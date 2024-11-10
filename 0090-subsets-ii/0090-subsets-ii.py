class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums.sort()
        for i in range(1<<n):
            v = ()
            for j in range(n):
                if (i &(1<<j)):
                    v += (nums[j],)
            
            ans.add(v)
        ans = list(ans)
        for i in range(len(ans)):
            ans[i] = list(ans[i])
        return ans
                    
        
        