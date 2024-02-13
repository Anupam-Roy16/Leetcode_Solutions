class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        v=[]
        nums.sort()
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                    l=(nums[i],nums[left],nums[right])
                    v.append(l)
                    left,right=left+1,right-1
                elif sum<0:
                    left=left+1
                else:
                    right=right-1
                #print(left,right)
        return list(set(v))
        #return list(v)
        