class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l <= r:
            m = l + (r-l)//2
            Lmin = matrix[m][0]
            Rmax = matrix[m][-1]
            if target < Lmin:
                r = m - 1
            elif target > Rmax:
                l = m + 1
            else:
                low = 0
                high = len(matrix[m])-1
                while low <= high:
                    mid = low + (high-low)//2
                    if matrix[m][mid] < target:
                        low = mid + 1
                    elif matrix[m][mid] > target:
                        high = mid - 1
                    else:
                        return True
                return False
        
        return False
