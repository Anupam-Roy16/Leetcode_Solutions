class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        flag = 1
        ans = []
        while n!=0:
            reminder = n%10
            n //=10
            num = reminder*flag
            if num != 0:
                ans.append(num)
            flag = flag*10
        return ans[::-1]


        