class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = set()
        for i in range(2,n+1):
            for j in range(1,i):
                global p,q
                if math.gcd(i,j)!=1:
                    p = i//gcd(i,j)
                    q = j//gcd(i,j)
                else:
                    p = i
                    q = j
                p = str(p)
                q = str(q)
                ss = q+"/"+p
                ans.add(ss)
        return list(ans) 
                
                    
        
        