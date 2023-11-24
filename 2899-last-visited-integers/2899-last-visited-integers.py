class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        num_list = []
        ans_list = []
        count_prev = 0
        length = len(words)
        for i in range(length):
            if words[i] != "prev":
                num_list.append(int(words[i]))
                count_prev = 0
            else:
                index = len(num_list)-1-count_prev
                if index<0:
                    ans_list.append(-1)
                else:
                    ans_list.append(num_list[index])
                count_prev += 1
        return ans_list
                
                
        