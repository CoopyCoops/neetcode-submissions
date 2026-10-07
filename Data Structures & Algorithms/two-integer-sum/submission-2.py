class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, n in enumerate(nums):
            index_map[n] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in index_map and index_map[difference] != i:
                return [i, index_map[difference]]
