class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        prefix = [0 for i in range(n)]
        suffix = [0 for i in range(n)]
        prefix[0] = height[0]
        suffix[n-1] = height[n-1]
        for i in range(1,n-1):
            prefix[i] = max(prefix[i-1], height[i])
        
        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1],height[i])

        for i in range(n):
            rain = min(prefix[i],suffix[i]) - height[i]
            if rain > 0: 
                ans += rain
        
        return ans