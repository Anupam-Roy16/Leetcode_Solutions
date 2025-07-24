class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency_dictionary = {}
        for letter in s:
            if letter in frequency_dictionary:
                frequency_dictionary[letter] +=1
            else:
                frequency_dictionary[letter] = 1
        max_odd ,answer= 0,0
        odd_found = False
        for frequency in frequency_dictionary.values():
            if frequency%2 == 0:
                answer += frequency
            elif max_odd < frequency:
                answer += (frequency-1)
                odd_found = True

        if odd_found:
            return answer +1
        else:
            return answer
        