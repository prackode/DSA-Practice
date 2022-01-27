# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur=prices[0];ans=0
        for i in prices:
            cur=min(cur,i)
            ans=max(ans,i-cur)
        return ans
