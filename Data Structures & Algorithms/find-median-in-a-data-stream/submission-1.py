class MedianFinder:

    def __init__(self):
        self.right = []
        self.left = []

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, -num)
        else:
            if self.right and num > self.right[0]:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)
            
        if len(self.right) - len(self.left) > 1:
            num = heapq.heappop(self.right)
            heapq.heappush(self.left, -num)
        elif len(self.left) - len(self.right) > 1:
            num = -heapq.heappop(self.left)
            heapq.heappush(self.right, num)


    def findMedian(self) -> float:
        if len(self.right) == len(self.left):
            return (self.right[0] - self.left[0]) / 2.0
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        