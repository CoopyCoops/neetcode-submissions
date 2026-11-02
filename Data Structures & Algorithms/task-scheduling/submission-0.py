class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxheap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()
        while maxheap or q:
            time += 1
            if maxheap:
                cnt = heapq.heappop(maxheap)
                cnt += 1
                if cnt < 0:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                task = q.popleft()
                heapq.heappush(maxheap, task[0])
        
        return time
