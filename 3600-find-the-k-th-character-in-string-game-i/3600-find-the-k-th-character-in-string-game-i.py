class Solution:
    def kthCharacter(self, k: int) -> str:
        s ="a"
        while 1:
            d = ""
            for x in s:
                f = ord(x)
                f+=1
                if x=='z':
                    f = ord('a')
                d+=chr(f)
            s+=d
            if len(s) >=k:
                break
        return s[k-1]



        