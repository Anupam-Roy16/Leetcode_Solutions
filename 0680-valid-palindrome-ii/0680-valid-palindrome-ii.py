class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            left , right = 0,len(s)-1
            while left < right:
                if s[left] != s[right]:
                    new_s_1 = s[:left] + s[left+1:]
                    new_s_2 = s[:right] + s[right+1:]
                    if new_s_1 == new_s_1[::-1] or new_s_2 == new_s_2[::-1]:
                        return True
                    else:
                        return False
                left +=1
                right -=1

        