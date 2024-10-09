#import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn = 1000000
        maxx= -1
        for x in nums:
            if minn > x:
                minn = x
            if maxx < x:
                maxx = x
        return math.gcd(minn,maxx)
                
            