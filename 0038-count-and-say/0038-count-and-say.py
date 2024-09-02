class Solution:
    def rle(self,s):
            ans =""
            i = 0
            while i < len(s):
                count = 0
                flag = -1
                for j in range(i+1,len(s)):
                    if s[i] == s[j]:
                        count += 1
                    else:
                        flag = j
                        break
                
                ans +=str(count+1)
                ans+=s[i]
                i = flag
                if flag == -1:
                    break
            return ans
        
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.rle(self.countAndSay(n-1))
        
        
                        
        
        