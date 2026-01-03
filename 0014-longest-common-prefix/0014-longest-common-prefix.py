class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # AR code
        strs.sort()
        size = len(strs[0])
        ans = ""
        for index in range(size):
            char = strs[0][index]
            print(char)
            for item in strs:
                if char != item[index]:
                    return ans
            ans +=strs[0][index]
        return ans 



       
       