class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        main_score = score[:]
        score_index_dic = {}
        score.sort(reverse = True)
        ans = []
        for i in range(len(score)):
            score_index_dic[score[i]] = i
        #print(score_index_dic)
        for i in range(len(score)):
            if score_index_dic[main_score[i]] == 0:
                ans.append("Gold Medal")
            elif score_index_dic[main_score[i]] == 1:
                ans.append("Silver Medal")
            elif score_index_dic[main_score[i]] == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(score_index_dic[main_score[i]]+1))
        return ans
        