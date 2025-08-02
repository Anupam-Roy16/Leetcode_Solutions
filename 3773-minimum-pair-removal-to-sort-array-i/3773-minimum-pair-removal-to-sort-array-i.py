class Solution:
    def helper(self,arr):
        if len(arr) == 1:
            return True
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True

    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while 1:

            if self.helper(nums) == True:
                return ans

            minn = 100000000000
            index = -1
            for i in range(len(nums)-1,0,-1):
                summ = nums[i] + nums[i-1]
                if (summ <=minn):
                    minn = summ
                    index = i
            nums = nums[:index-1] + [nums[index] + nums[index-1]]+ nums[index+1:]
            print(nums)
            ans +=1
            


        