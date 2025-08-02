class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        frequency_dictionary = {}
        for x in s:
            if x in frequency_dictionary:
                frequency_dictionary[x] +=1
            else:
                frequency_dictionary[x] = 1
        def sorting_fucntion(tmp):
            return tmp[1]
        sorted_frequency_dictionary = dict(sorted(frequency_dictionary.items(),key=sorting_fucntion))
        number_of_distinct = len(sorted_frequency_dictionary)
        if number_of_distinct <=k:
            return 0
        else:
            count_deletion = number_of_distinct - k
            ans = 0
            for val in sorted_frequency_dictionary.values():
                ans += val
                count_deletion -=1
                if count_deletion ==0:
                    return ans  

        