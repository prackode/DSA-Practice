# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        ans=[]
        n=len(nums)
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]>(n//3):
                ans.append(i)
        return ans