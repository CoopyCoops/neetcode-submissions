class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if freq.get(num, 0) != 0:
                return True
            freq[num] = 1 + freq.get(num, 0)

        return False