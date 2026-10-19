class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(heights[0],0)]
        maxArea = 0

        for i in range(1,len(heights)):
            height = heights[i]
            if height <= stack[-1][0]:
                while stack and height <= stack[-1][0]:
                    x = stack.pop()
                    h = x[0]
                    idx = x[1]
                    maxArea = max(maxArea, h*(i-idx))
                stack.append((height,idx))
            else:
                stack.append((height,i))

        for i in range(len(stack)):
            x = stack.pop()
            h = x[0]
            idx = x[1]
            maxArea = max(maxArea, h*(len(heights)-idx))
        
        return maxArea