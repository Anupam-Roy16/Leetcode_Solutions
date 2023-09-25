class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        profit=0
        r=len(prices)-1
        while i<r:
            while(i<r and prices[i+1]<=prices[i]):
                i+=1
            buy=prices[i]
            while(i<r and prices[i+1]>prices[i]):
                i+=1
            sell=prices[i]
            profit+=(sell-buy)
        return profit
        