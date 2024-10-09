class Solution:
    def primility_test(self,n):
        if n<2:
            return False
        for i in range(2,int(n**.5)+1):
            if n%i == 0:
                return False
        return True
                
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        maxx = 0
        row = len(nums)
        col = len(nums[0])
        for i in range(row):
            for j in range(col):
                if i==j:
                    if self.primility_test(nums[i][i]):
                        #print(nums[i][i],"sd")
                        if maxx < nums[i][i]:
                            maxx = nums[i][i]
                elif j == row-i-1:
                    if self.primility_test(nums[i][row-i-1]):
                        if maxx < nums[i][row-i-1]:
                            maxx = nums[i][row-i-1]
        return maxx
                    
                        
                    
        
        
        