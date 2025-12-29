class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            temp_list = []
            while x:
                rem = x%10
                temp_list.append(rem)
                x /=10
                x = int(x)
            size = len(temp_list)
            left , right = 0,size-1
            print(temp_list)
            while left<right:
                if temp_list[left] != temp_list[right]:
                    return False
                left,right =left+1,right-1
            return True



        