class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            flag = 1 << i
            count1 = 0
            for j in range(len(nums)):
                if (nums[j] & flag):
                    count1 +=1
            count0 = len(nums) - count1
            for j in range(len(nums)):
                if (nums[j] & flag ):
                    ans += count0
                    count1 -= 1
                else:
                    ans += count1
                    count0 -= 1
        return ans


        