class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        n = len(nums)//3
        ans = []
        s = set()
        for x in nums:
            if x not in dic:
                dic[x] =1
            else:
                dic[x] +=1
            if dic[x] > n:
                s.add(x)
        return list(s)
        