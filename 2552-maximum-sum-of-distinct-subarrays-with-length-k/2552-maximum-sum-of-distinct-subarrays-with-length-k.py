import heapq
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        tmp = [nums[0]]
        for i in range(k):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]] = 1
        for i in range(1,len(nums)):
            tmp.append(tmp[i-1]+nums[i])
        maxx = 0
        if len(d) == k:
            if maxx < tmp[k-1]:
                maxx = tmp[k-1]
        j ,i= k ,0
        while j<len(nums):
            if nums[j] in d:
                d[nums[j]] += 1
            else:
                d[nums[j]] = 1
            if nums[i] in d:
                if d[nums[i]] ==1:
                    del d[nums[i]]
                else:
                    d[nums[i]] -=1
            if len(d) == k:
                if maxx <(tmp[j] - tmp[i]):
                    maxx = tmp[j] - tmp[i]     
            
            j+=1
            i+=1
        return maxx

       