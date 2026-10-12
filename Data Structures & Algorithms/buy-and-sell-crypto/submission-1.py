class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(1,len(prices)):
            maxprofit = max(prices[i] - min(prices[0:i]), maxprofit)
        
        return maxprofit