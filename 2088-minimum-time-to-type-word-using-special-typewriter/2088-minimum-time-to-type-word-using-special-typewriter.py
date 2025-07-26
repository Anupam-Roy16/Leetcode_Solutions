class Solution:
    def minTimeToType(self, word: str) -> int:
        current_char = 'a'
        ans = 0
        for x in word:
            temp1 = abs(ord(current_char) - ord(x))
            temp2 = 26 - temp1
            #print(temp1,temp2)
            ans+= (min(temp1, temp2)+1)
            current_char = x
        return ans

        