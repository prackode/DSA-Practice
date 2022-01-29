# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        cur = []
        st = intervals[0][0]
        ed = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ed:
                if ed < intervals[i][1]:
                    ed = intervals[i][1]
            else:
                ans.append([st, ed])
                st = intervals[i][0]
                ed = intervals[i][1]
        ans.append([st, ed])
        return ans
