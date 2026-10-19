class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1
        low = 0

        while low <= high:
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                high = mid - 1
                mid = (low+high)//2
            else:
                low = mid + 1
                mid = (low+high)//2
        
        return -1