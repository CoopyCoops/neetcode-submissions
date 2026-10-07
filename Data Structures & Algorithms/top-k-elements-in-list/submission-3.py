class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        freq = [[] for i in range(len(nums)+1)]
        for num, count in count_dict.items():
            freq[count].append(num)

        ans = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans