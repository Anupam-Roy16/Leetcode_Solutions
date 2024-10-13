class Solution:
    def primility_test(self,n):
        if n<2:
            return False
        elif n==2:
            return True
        else:
            for i in range(2,int(n**.5)+1):
                if n%i ==0:
                    return False
            return True
        
    def nonSpecialCount(self, l: int, r: int) -> int:
        ans = 0
        if l**.5 != int(l**.5):
            left = int(l**.5)+1
        else:
            left = int(l**.5)
            
        if r**.5 != int(r**.5):
            right = int(r**.5)
        else:
            right = int(r**.5)
       # print(left,right)
        for i in range(left,right+1):
            if self.primility_test(i):
                ans +=1
       # print(ans)
        return r-l+1-ans
        