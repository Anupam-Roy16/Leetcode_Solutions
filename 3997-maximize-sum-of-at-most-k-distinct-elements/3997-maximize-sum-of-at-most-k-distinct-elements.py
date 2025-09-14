class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse= True)
        ans = []
        count = 0
        for x in nums:
            if x not in ans:
                ans.append(x)
                count+=1
            if count == k:
                break
        return ans