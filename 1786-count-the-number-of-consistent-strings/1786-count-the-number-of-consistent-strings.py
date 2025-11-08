class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            flag = 0
            for x in word:
                if x not in allowed:
                    flag = 1
                    break
            if flag == 0:
                ans +=1
        return ans
            





        