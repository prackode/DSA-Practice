# https://leetcode.com/problems/unique-paths/
# using memoization (simplest DP)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        adj = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            adj[i][0] = 1
        for i in range(n):
            adj[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                adj[i][j] = adj[i-1][j]+adj[i][j-1]
        return adj[m-1][n-1]
