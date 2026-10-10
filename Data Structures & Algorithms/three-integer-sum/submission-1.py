class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1,len(nums)-1
            target = -nums[i]
            while j < k:
                tot = nums[j] + nums[k]
                if tot < target:
                    j += 1
                elif tot > target:
                    k -= 1
                else:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        
        return list(ans)