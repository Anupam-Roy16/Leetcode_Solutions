class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)-1
        flag = 0
        for i in range(size,0,-1):
            if nums[i]>nums[i-1]:
                minn = 100000000000
                j = -1
                index = -1
                for j in range(i,size+1):
                    if nums[i-1] < nums[j]:
                        if minn > nums[j]:
                            minn = nums[j]
                            index = j
                #print()
                tmp = nums[index]
                nums[index] = nums[i-1]
                nums[i-1] = tmp
                print(nums)
                tmp = nums[i:]
                tmp.sort()
                nums[:] = nums[:i] + tmp
                flag = 1
                break 
        if flag ==0:
            nums[:] = nums[::-1]
            
        