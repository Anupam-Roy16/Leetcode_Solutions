class Solution:
    def splitArray(self, nums: List[int]) -> int:
        inc_val = [1]
        flag = 1
        for i in range(1,len(nums)):
            if flag == 1:
                if nums[i] > nums[i-1]:
                    inc_val.append(1)
                else:
                    inc_val.append(0)
                    flag = 0
            elif flag == 0:
                inc_val.append(0)
        dec_val = [1]
        flag = 1
        for i in range(len(nums)-2,-1,-1):
            if flag ==1:
                if nums[i] >nums[i+1]:
                    dec_val.append(1)
                else:
                    dec_val.append(0)
                    flag = 0
            elif flag == 0:
                dec_val.append(0)
        dec_val = dec_val[::-1]
        prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[i-1])
        
        total = prefix_sum[-1]
        minn = 1000000000000
        for i in range(len(nums)-1):
            if inc_val[i] and dec_val[i+1]:
                temp = abs(prefix_sum[i]-(total-prefix_sum[i]))
                if minn > temp:
                    minn = temp
        if minn == 1000000000000:
            return -1
        return minn 


        

    
        





        