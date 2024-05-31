class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        while i < j:
            if not(s[i]>='a' and s[i]<='z') and not(s[i]>='A' and s[i]<='Z') and not(s[i]>='0' and s[i]<='9'):
                i+=1
                continue
            if not(s[j]>='a' and s[j]<='z') and not(s[j]>='A' and s[j]<='Z') and not(s[j]>='0' and s[j]<='9'):
                j -= 1
                continue
            p = s[i]
            q = s[j]
            if s[i]>='A' and s[i]<='Z':
                p = chr(ord(s[i]) +ord('a')-ord('A'))
            if s[j]>='A' and s[j]<='Z':
                q = chr(ord(s[j]) +ord('a')-ord('A'))
            if (p != q):
                return False
            else:  
                i+=1
                j-=1
        return True