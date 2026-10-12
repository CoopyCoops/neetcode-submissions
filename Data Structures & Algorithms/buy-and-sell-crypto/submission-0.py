class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            maxprofit = max(prices[i] - min(prices[0:i]), maxprofit)
        
        return maxprofit