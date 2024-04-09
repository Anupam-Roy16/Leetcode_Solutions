class Solution:
    def fun(self,num):
        var = str(num)
        for s in var:
            if s == '0' or num% int(s) != 0:
                return 0
        return 1
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left,right+1):
            if self.fun(num):
                ans.append(num)
        return ans