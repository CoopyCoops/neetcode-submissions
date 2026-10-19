class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m] > nums[m+1]:
                return nums[m+1]
            elif nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m - 1
            else:
                return nums[0]
