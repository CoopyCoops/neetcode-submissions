class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]

        prefix = {}
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix.get(i-1, 1)
        
        suffix = {}
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i+1] * suffix.get(i+1, 1)
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[i])
            elif i == len(nums) - 1:
                res.append(prefix[i])
            else:
                res.append(suffix[i] * prefix[i])
        
        return res