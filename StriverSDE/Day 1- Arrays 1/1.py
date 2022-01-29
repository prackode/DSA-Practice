# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r,c=[],[]
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        for i in r:
            for j in range(m):
                matrix[i][j]=0
        for i in range(n):
            for j in c:
                matrix[i][j]=0
