class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        size = len(nums)
        count = 0
        for i in range(size-1):
            for j in range(i+1,size):
                temp = str(nums[i])
                temp1 = int(temp[0])
                temp2 = nums[j] % 10
                if math.gcd(temp2,temp1)==1:
                    count+=1
        return count
        