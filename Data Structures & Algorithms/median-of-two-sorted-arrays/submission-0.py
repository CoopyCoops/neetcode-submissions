class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2))//2
        maxLeft = float("-inf")
        minRight = float("inf")
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l,r = 0,len(nums1)

        while l <= r:
            i = l + (r-l)//2
            j = half - i
            
            # Greatest element on the left side
            aLeft = nums1[i-1] if i > 0 else float("-inf")
            bLeft = nums2[j-1] if j > 0 else float("-inf")

            # Smallest element on the right side
            aRight = nums1[i] if i < len(nums1) else float("inf")
            bRight = nums2[j] if j < len(nums2) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return float(min(aRight,bRight))
                else:
                    return (min(aRight,bRight) + max(aLeft,bLeft)) / 2
            elif aRight < bLeft:
                l = i + 1
            else:
                r = i - 1
        
        if (len(nums1) + len(nums2)) % 2 == 1:
            return minRight
        else:
            return (maxLeft + minRight) / 2