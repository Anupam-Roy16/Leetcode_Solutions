class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        dic={}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if s[i] not in dic.values():
                    dic[pattern[i]] = s[i]
                else:
                    return False
            elif dic[pattern[i]] != s[i]:
                return False
        return True
            