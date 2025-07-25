class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        original_absolute_arr = []
        for x in nums:
            if x<0:
                original_absolute_arr.append([x,-1*x])
            else:
                original_absolute_arr.append([x,x])
        def sorting_fun(arr):
            return -arr[1]
        sorted_original_absolute_arr = sorted(original_absolute_arr,key = sorting_fun)
        for num in sorted_original_absolute_arr:
            if num[0] < 0:
                if k>0:
                    num[0] = -1* num[0]
                    k-=1
                else:
                    break
        if k >0:
            if k%2 !=0:
                sorted_original_absolute_arr[len(nums)-1][0] = -1*sorted_original_absolute_arr[len(nums)-1][0]
            # for num in sorted_original_absolute_arr[::-1]:
            #     if k>0:
            #         num[0] = -1*num[0]
            #         k-=1
            #     else:
            #         break
        ans = 0
        for num in sorted_original_absolute_arr:
            ans+= num[0]
        return ans

        
        