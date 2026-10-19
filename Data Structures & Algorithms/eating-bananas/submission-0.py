class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        ans = high
        while low <= high:
            mid = low + (high-low)//2
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas/mid)
            if hours <= h:
                ans = min(mid,ans)
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
