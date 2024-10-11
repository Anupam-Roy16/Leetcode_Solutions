class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = []
        for i in range(1,int(n**.5)+1):
            if n%i==0:
                if i == n//i:
                    ans.append(i)
                else:
                    ans.append(i)
                    ans.append(n//i)
        ans.sort()
        if k > len(ans):
            return -1
        return ans[k-1]
            
                
                
            
        