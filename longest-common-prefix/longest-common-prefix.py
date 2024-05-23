class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        i = 0
        if len(strs)==1:
            return strs[0]
        while 1:
            flag =0
            for j in range(1,len(strs)):
                if len(strs[j])-1<i or len(strs[0])-1<i:
                    flag = 1
                    break
                if strs[j][i] != strs[0][i]:
                    flag = 1
                    break
            #print(flag)
            if flag == 0:
                s +=strs[0][i]
            else:
                return s
            i+=1
            
        