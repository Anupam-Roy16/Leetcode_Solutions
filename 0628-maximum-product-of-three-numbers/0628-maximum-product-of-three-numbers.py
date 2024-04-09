class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        'trick: consider the case -9 -8 -1 0 1 2 3'
        nums.sort()
        length = len(nums) -1
        product1 =-100000000000
        if nums[0]<0 and nums[1] < 0 and nums[length] >0:
            product1 = nums[0] * nums[1] * nums[length]
        product2 = nums[length-2] * nums[length-1] * nums[length]
        return max(product1,product2)
           