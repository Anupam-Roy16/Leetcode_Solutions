class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ans_dict = {}
        for item in items1:
            if item[0] in ans_dict:
                ans_dict[item[0]] += item[1]
            else:
                ans_dict[item[0]] = item[1]
        for item in items2:
            if item[0] in ans_dict:
                ans_dict[item[0]] += item[1]
            else:
                ans_dict[item[0]] = item[1]
        #ans_dict.sort()
        ans = []
        for key , val in ans_dict.items():
            ans.append([key,val])
        ans.sort()
        return ans
        