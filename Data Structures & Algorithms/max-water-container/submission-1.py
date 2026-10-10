class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        area = 0

        while l < r:
            height = min(heights[l], heights[r])
            width = r-l
            area = max(height * width, area)
            if heights[r] > heights[l]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[r-1] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return area