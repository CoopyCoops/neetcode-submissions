class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]

        freq, idx = 0, []
        for i in range(len(nums)):
            if nums[i] == 0:
                freq += 1
                idx.append(i)
            if freq == 2:
                return [0 * i for i in range(len(nums))]
        if freq == 1:
            index = idx[0]
            total_product = 1
            for i in range(len(nums)):
                if i == index:
                    continue
                total_product *= nums[i]
            res = [0 * i for i in range(len(nums))]
            res[index] = total_product
            return res
        else:
            res = []
            total_product = 1
            for i in range(len(nums)):
                total_product *= nums[i]
            for i in range(len(nums)):
                res.append(total_product // nums[i])
        
        return res