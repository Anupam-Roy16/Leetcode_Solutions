class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tem_list = [0]*(len(nums))
        tem_list[0]=nums[0]
        for i in range(1,len(nums)):
            tem_list[i] = nums[i] + tem_list[i-1]
        max_sum  = -900000000000000000000000000
        flag = 0
        print(tem_list)
        for i in range(k-1,len(nums)):
            if flag == 0:
                flag = 1
                if tem_list[i] > max_sum:
                    max_sum = tem_list[i]
            else:
                if (tem_list[i] - tem_list[i-k])>max_sum:
                    max_sum = tem_list[i] - tem_list[i-k]
        return max_sum/k
        