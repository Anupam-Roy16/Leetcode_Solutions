class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        for i in range(1,46342):
            if i*i == num:
                return True
            elif i*i > num:
                break
        return False
        