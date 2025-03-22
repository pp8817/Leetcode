class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        temp = prices[0]
        for p in prices:
            if temp > p:
                temp = p
                
            profit = p - temp
            if profit > result:
                result = profit

        return result