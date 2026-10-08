class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        nums.sort()
        i,j,count = 0,1,1
        while j < len(nums):
            temp = 1
            if nums[j] - nums[i] != 1:
                i += 1
                j += 1
            while j < len(nums) and nums[j] - nums[i] == 1:
                temp += 1
                j += 1
                i += 1
                if j < len(nums) and nums[j] == nums[i]:
                    j += 1
                    i += 1
            count = max(temp, count)
            
        return count