class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            if x in dic:
                dic[x] +=1
            else:
                dic[x] = 1
        ans = 0
        for x in dic.keys():
            if dic[x] == 2:
                ans = ans^x
        return ans
        