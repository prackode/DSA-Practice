# https://leetcode.com/problems/majority-element/
# Moore's voting algorithm
# O(1) space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        cnt = 1
        n = len(nums)
        for i in range(1, n):
            if cnt == 0:
                ans = nums[i]
                cnt += 1
            elif nums[i] == ans:
                cnt += 1
            else:
                cnt -= 1
        return ans
