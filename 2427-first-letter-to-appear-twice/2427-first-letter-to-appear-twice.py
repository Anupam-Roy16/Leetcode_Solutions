class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]].append(i)
            else:
                dic[s[i]] = [i]
        for i in range(len(s)):
            if len(dic[s[i]]) > 1:
                flag = 0
                for j in range(i+1,len(s)):
                    if len(dic[s[j]])>1:
                        if dic[s[i]][1] > dic[s[j]][1]:
                            flag = 1
                            break
                if flag == 0:
                    return s[i]
                    


        