class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = []
        for ind, num in enumerate(nums):
            index_map.append([num, ind])

        index_map.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            value = index_map[i][0] + index_map[j][0]
            if value == target:
                first = min(index_map[i][1], index_map[j][1])
                second = max(index_map[i][1], index_map[j][1])
                return [first, second]
            elif value > target:
                j -= 1
            else:
                i += 1