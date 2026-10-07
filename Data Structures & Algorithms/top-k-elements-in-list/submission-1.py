class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for i in range(len(nums)):
            if nums[i] in count_dict:
                count_dict[nums[i]] += 1
            else:
                count_dict[nums[i]] = 1
        
        count_dict_sorted = dict(sorted(count_dict.items(),
                            key = lambda item: item[1], reverse = True))
        ans = []
        i = 0
        for key, value in count_dict_sorted.items():
            ans.append(key)
            i += 1
            if i == k:
                break

        return ans