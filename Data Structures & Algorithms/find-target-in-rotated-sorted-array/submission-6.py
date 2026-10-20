class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        l,r = 0,len(nums)-1

        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[m+1]:
                mid = m+1
                break
            elif nums[m] < nums[m-1]:
                mid = m
                break
            elif nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m - 1
            else:
                mid = 0
                break
                
        if nums[mid] == target:
            return mid
        elif mid == 0:
            l,r = 0,len(nums)-1
            while l <= r:
                m = l + (r-l)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
        else:
            l,r = mid+1,len(nums)-1
            while l <= r:
                m = l + (r-l)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
        
            l,r = 0,mid-1
            while l <= r:
                m = l + (r-l)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
        
        return -1