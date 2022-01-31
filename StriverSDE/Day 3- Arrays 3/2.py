# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        ch = 0
        if n < 0:
            ch = 1
        n = abs(n)
        if not x:
            return 0
        while n:
            if n & 1:
                res *= x
            n >>= 1
            x *= x
        if ch:
            return 1/res
        return res
