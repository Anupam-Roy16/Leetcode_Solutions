class Solution:
    def integerReplacement(self, n: int) -> int:
        map = {}
        def fun(n):
            if n == 1:
                return 0
            elif n%2==0:
                return 1 + fun(n//2) 
            else:
                return 1+ min(fun(n+1),fun(n-1))
        return fun(n)
            





        