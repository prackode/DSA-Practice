# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        ans=[[] for i in range(n)]
        ans[0]=[1]
        for i in range(1,n):
            ans[i].append(1)
            for j in range(1,len(ans[i-1])):
                cur=ans[i-1][j]+ans[i-1][j-1]
                ans[i].append(cur)
            ans[i].append(1)
        return ans
