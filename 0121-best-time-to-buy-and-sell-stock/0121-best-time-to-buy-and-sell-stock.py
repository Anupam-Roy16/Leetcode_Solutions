class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #AR CODE
        min_num = 1111111111111111
        max_profit = 0
        for price in prices:
            if min_num < price:
                if max_profit < price - min_num:
                    max_profit = price - min_num
            if price < min_num:
                min_num = price
        return max_profit
            


        