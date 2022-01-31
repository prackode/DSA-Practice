# https://leetcode.com/problems/search-a-2d-matrix/
# O(log(m)+log(n))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n-1
        row = -1
        while l <= r:
            mid = (l+r) >> 1
            if matrix[mid][0] <= target and target <= matrix[mid][m-1]:
                row = mid
                break
            if matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid+1
        if row == -1:
            return 0
        l, r = 0, m-1
        while l <= r:
            mid = (l+r) >> 1
            if matrix[row][mid] == target:
                return 1
            if matrix[row][mid] > target:
                r = mid-1
            else:
                l = mid+1
        return 0
