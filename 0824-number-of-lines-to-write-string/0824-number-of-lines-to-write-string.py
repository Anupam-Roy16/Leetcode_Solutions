class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        count = 0
        ans1 = 0
        ans2 = 0
        for i in range(len(s)):
            count += widths[ord(s[i])-ord('a')]
            if count==100:
                if i ==(len(s)-1):
                    ans2 = count
                count =0
                ans1+=1
            elif count>100:
                

                count = widths[ord(s[i])-ord('a')]
                ans1+=1
                if i ==(len(s)-1):
                    ans2 = count
                    ans1 +=1
            else:
                if i ==(len(s)-1):
                    ans2 = count
                    ans1+=1

        return [ans1,ans2]
            
        
            





        