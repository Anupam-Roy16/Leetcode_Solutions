class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counting_dict = dict()
        for x in nums:
            if x in counting_dict:
                counting_dict[x]+=1
            else:
                counting_dict[x] = 1
        for i in range(len(nums)):
            if 0 in counting_dict and counting_dict[0] != 0:
                nums[i] = 0
                counting_dict[0] -=1
            elif 1 in counting_dict and counting_dict[1] !=0:
                nums[i] = 1
                counting_dict[1] -=1
            elif 2 in counting_dict and counting_dict[2] !=0:
                nums[i] =2
                counting_dict[2] -=1
        