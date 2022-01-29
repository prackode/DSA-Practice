# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero=0;one=0
        n=len(nums)
        for i in nums:
            if i==0: zero+=1
            if i==1: one+=1
        i=0
        while zero:
            nums[i]=0
            zero-=1;i+=1
        while one:
            nums[i]=1
            one-=1;i+=1
        while i<n:
            nums[i]=2
            i+=1
