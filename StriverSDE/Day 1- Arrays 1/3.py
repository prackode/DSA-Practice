# https://leetcode.com/problems/next-permutation/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma,mx=-10**5,0
        for i in range(len(nums)):
            mx+=nums[i]
            ma=max(mx,ma)
            mx=max(0,mx)
        return ma
