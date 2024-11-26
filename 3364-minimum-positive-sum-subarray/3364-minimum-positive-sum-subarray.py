class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        tmp = []
        for x in nums:
            tmp.append(x)
        if len(nums)!=1:
            for i in range(1,len(nums)):
                nums[i] += nums[i-1]
        minn = 100000000000
        print(nums,tmp)
        for i in range(l,r+1):
            fast ,sec= 0 , i-1
            if fast == sec:
                for x in tmp:
                    if x>0 and x < minn:
                        minn = x
                print(minn)
                continue
            
            while sec < len(nums) and fast-1 >=-1 :
                if (fast-1)==-1:
                    tmp = nums[sec]
                    print(tmp)
                else: 
                    tmp = (nums[sec]-nums[fast-1])
               
                print(nums[fast],nums[sec],tmp)
                if tmp>0 and  minn > tmp:
                    minn = tmp
                sec+=1
                fast+=1
        if minn == 100000000000:
            return -1
        else:
            return minn
                    
                    
                
                
        
            
        