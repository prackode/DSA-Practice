# https://leetcode.com/problems/find-the-duplicate-number/
# Using Floyd's cycle detection algo

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0;j = 0
        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break
        j = 0
        while True:
            j = nums[j]
            i = nums[i]
            if i == j:
                return i
