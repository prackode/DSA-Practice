# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n-1, -1, -1):
                val = matrix[i].pop()
                matrix[j].insert(0, val)
