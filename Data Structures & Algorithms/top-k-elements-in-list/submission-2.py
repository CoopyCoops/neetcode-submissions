class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        heap = []
        for num, freq in count_dict.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans