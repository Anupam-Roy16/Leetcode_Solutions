class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        v=[]
        nums.sort()
        i = 0 
        while i < len(nums)-2:
            left,right=i+1,len(nums)-1
            print(i,"we")
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                #print(left,right)
                if sum==0:
                    l=[nums[i],nums[left],nums[right]]
                    #print(l)
                    v.append(l)
                    while (left+1)<len(nums) and  nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    while right-1>=0 and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                elif sum<0:
                    left=left+1
                else:
                    right=right-1
                #print(left,right)
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i +=1
            i += 1
            
        return v
        #return list(v)
        