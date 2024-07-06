class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        for x in ransomNote:
            if x in dict1:
                dict1[x] += 1
            else:
                dict1[x] = 1
        dict2 ={}
        for x in magazine:
            if x in dict2:
                dict2[x] += 1
            else:
                dict2[x] = 1
        for x in dict1:
            if x not in dict2:
                return False
            else:
                if dict1[x] > dict2[x]:
                    return False
        return True