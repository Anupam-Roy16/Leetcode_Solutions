class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1,int(n**.5)+1):
            if n%i==0:
                if i == n//i:
                    count += 1
                else:
                    count += 2
        if count == 3:
            return True
        else:
            return False
        
        
        