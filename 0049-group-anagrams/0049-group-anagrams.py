class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_dict = {}
        for x in strs:
            temp = x
            x = list(x)
            x.sort()
            s = ""
            s = s.join(x)
            if s not in temp_dict:
                temp_dict[s] = [temp]
            else:
                temp_dict[s]+=[temp]
        ans = []
        for x in temp_dict.values():
            ans.append(x)
        return ans
