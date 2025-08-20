class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        #paragraph = paragraph.split()
        tmp = []
        import re
       
        tmp = re.split(r'[^\w]+', paragraph)
        
        ans =""
        maxx = 0
        print(tmp)
        for s in tmp:
            if s!="" and s not in banned:
                if tmp.count(s) >= maxx:
                    ans = s
                    maxx = tmp.count(s)
        return ans
                

        