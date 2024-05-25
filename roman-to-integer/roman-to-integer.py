class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        dict ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if len(s)==1:
            return dict[s[0]]
        i =0
        while i < (len(s)-1):
            if s[i] == 'I':
                if s[i+1] =='V':
                    ans += 4
                    i += 2
                elif s[i+1] =='X':
                    ans += 9
                    i += 2
                else:
                    ans += 1
                    i+=1
            elif s[i] == 'X':
                if s[i+1] =='L':
                    ans += 40
                    i += 2
                elif s[i+1] =='C':
                    ans += 90
                    i += 2
                else:
                    ans += 10
                    i+=1
            elif s[i] == 'C':
                if s[i+1] =='D':
                    ans += 400
                    i += 2
                elif s[i+1] =='M':
                    ans += 900
                    i += 2
                else:
                    ans += 100
                    i+=1
            else:
                ans += dict[s[i]]
                i+=1
        if i == len(s)-1:
            ans += dict[s[i]]
        return ans