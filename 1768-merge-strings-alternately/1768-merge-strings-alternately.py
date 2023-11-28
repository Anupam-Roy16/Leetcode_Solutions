class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        s=""
        j,k,r,d=0,0,0,0
        while(1):
            if i%2==0 and r == 0:
                s += word1[j]
                j += 1
                if j>=len(word1):
                    r += 1
            elif d==0:
                s += word2[k]
                k += 1
                if k>=len(word2):
                    d += 1
            if r==1 and d==1:
                break
            i += 1
        return s
                
        
        