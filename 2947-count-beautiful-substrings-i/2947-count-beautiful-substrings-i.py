class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        d = {}
        v, c= 0 , 0
        d[-1] =[0,0]
        for i in range(len(s)):
            if s[i] =='a' or s[i] =='e' or s[i] =='i' or s[i] =='o' or s[i] == 'u':
                v += 1
            else:
                c += 1
            d[i]=[v,c]
        count =0
        for i in range(len(s)):
            for j in range(i,len(s)):
                v = -d[i-1][0] + d[j][0]
                c = -d[i-1][1] + d[j][1]
                if v == c and (v*c)%k == 0:
                    count+=1

        return count        
        