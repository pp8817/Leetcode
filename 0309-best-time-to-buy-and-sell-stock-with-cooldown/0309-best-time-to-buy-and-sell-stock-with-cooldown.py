# 상태 3가지
## 1. 주식을 구매하는 상태
## 2. 주식을 파는 상태
## 3. 주식을 들고 있지 않은 상태 (cooltime)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        buy = -prices[0] # 주식을 구매한 상태
        sell = 0 # 주식을 판 상태
        cooltime = 0 # 주식을 들고 있지 않은 상태

        for i in range(1, len(prices)):
            prev_buy = buy
            prev_sell = sell
            prev_cooltime = cooltime

            # 주식을 구매한 상태
            ## 1. 오늘 주식을 구매한다.
            ## 2. 아무것도 하지 않고 넘어간다.
            buy = max(prev_cooltime - prices[i], prev_buy)

            # 주식을 판 상태
            sell = prev_buy + prices[i]

            # 주식을 들고 있지 않은 상태
            ## 1. 오늘도 아무 행동을 하지 않는다.
            ## 2. 어제 주식을 판 경우
            cooltime = max(prev_cooltime, prev_sell)
    
        return max(sell, cooltime)
