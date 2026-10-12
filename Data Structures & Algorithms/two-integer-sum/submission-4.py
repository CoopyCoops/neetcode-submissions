class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxmap = []
        for idx, num in enumerate(nums):
            idxmap.append([num, idx])
        
        idxmap.sort()

        i,j = 0,len(nums)-1

        while i < j:
            value = idxmap[i][0] + idxmap[j][0]
            if value == target:
                first = min(idxmap[i][1], idxmap[j][1])
                second = max(idxmap[i][1], idxmap[j][1])
                return [first, second]
            elif value < target:
                i += 1
            else:
                j -= 1