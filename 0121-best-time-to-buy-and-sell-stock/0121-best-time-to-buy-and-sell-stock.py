class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        max=-1000000
        while r<len(prices):
            e=prices[r]-prices[l]
            if max<e:
                max=e
            if e<0:
                l=r
                r+=1
            else:
                r+=1
        if max<0:
            return 0
        else:
            return max
            
        