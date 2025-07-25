class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_x , count_r,ans = 0,0,0
        for x in s:
            if x !='R':
                count_x +=1
            else:
                count_r +=1
            if count_x == count_r:
                ans+=1
                count_x , count_r = 0,0
        return ans

        