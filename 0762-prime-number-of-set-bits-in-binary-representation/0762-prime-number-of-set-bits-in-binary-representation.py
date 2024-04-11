class Solution:
    def count_set_bit(self,num):
        const = 1
        count, i = 0 , 0 
        while num:
            if num & const:
                count += 1
            num = num >> 1
        return count
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = [2,3,5,7,11,13,17,19,23]
        ans =0
        for x in range(left , right+1):
            if self.count_set_bit(x) in prime:
                ans +=1
        return ans