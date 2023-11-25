class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        words_1 = []
        words_2 = []
        flag_1 = 0
        flag_2 = 1
        for i in range(len(groups)):
            if groups[i] == flag_1:
                if flag_1 == 0:
                    flag_1 = 1
                else:
                    flag_1 = 0
                words_1.append(words[i])
            if groups[i] == flag_2:
                if flag_2 == 0:
                    flag_2 = 1
                else:
                    flag_2 = 0
                words_2.append(words[i])
        if len(words_1)>len(words_2):
            return words_1
        else:
            return words_2
                
        
        