# https://leetcode.com/problems/reverse-pairs/
# using merge sort

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def f(arr, n, s, e):
            if (n == 1):
                return 0
            mid = (s + e) // 2
            f1 = sorted(arr[s: mid + 1])
            f2 = sorted(arr[mid + 1: e+1])
            combi, i, j = 0, 0, 0
            fL = mid - s + 1
            sL = e - mid
            while (i < fL):
                combi += j
                while (j < sL):
                    if (2 * f2[j] < f1[i]):
                        combi += 1
                        j += 1
                    else:
                        break
                i += 1
            p1 = f(arr, mid - s + 1, s, mid)
            p2 = f(arr, e - mid, mid + 1, e)
            return combi+p1+p2
        n = len(nums)
        return f(nums, n, 0, n-1)
