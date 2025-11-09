class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        size = len(nums)
        ans = 0
        for i in range(1, 1<<size):
            num = i
            pos = 0
            tmp_ans = 0
            while num:
                if num & 1:
                    tmp_ans^=nums[pos]
                num = num>>1
                pos+=1
            ans +=tmp_ans
        return ans



        