class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lic = licensePlate.lower()
        has = dict()
        for s in lic:
            if 'a'<=s<='z':
                if s in has:
                    has[s]+=1
                else:
                    has[s] = 1
        minn = 10000000000000
        for word in words:
            tmp = has.copy()
            for s in word:
                if s in tmp:
                    tmp[s] -=1
                    if tmp[s] == 0:
                        del tmp[s]
                if len(tmp) == 0:
                    if len(word) < minn:
                        minn = len(word)
                        ans = word
        return ans


                    






        