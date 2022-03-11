from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        temp = intervals[0]
        ans = 0
        for i in range(1, len(intervals)):
            a, b = temp
            c, d = intervals[i]
            if a <= c and b >= d:
                ans += 1
                print(temp, intervals[i])
            else:
                temp = intervals[i]
                
        return len(intervals) - ans

sol = Solution()
intervals = [[1,4],[3,6],[2,8]]
intervals = [[1,4],[2,3]]
# intervals = [[0,10],[5,12]]
# intervals = [[1,2],[1,4],[3,4]]
print(sol.removeCoveredIntervals(intervals))
