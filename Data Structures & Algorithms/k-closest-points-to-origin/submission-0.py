class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            dist = math.sqrt(x1**2 + y1**2)
            heapq.heappush(minheap, (-dist, points[i]))
            if len(minheap) > k:
                heapq.heappop(minheap)

        ans = []
        for i in range(len(minheap)):
            dist, coordinates = heapq.heappop(minheap)
            ans.append(coordinates)

        return ans