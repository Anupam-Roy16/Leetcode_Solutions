class Solution:   
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min1 = 100000000
        min2 = 100000000
        if len(ops) == 0:
            return m*n
        for var in ops:
            if min1 > var[0]:
                min1 = var[0]
            if min2 > var[1]:
                min2 = var[1]
        
        return min1*min2
            
        