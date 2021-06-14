from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        print(ranges)
        left_count_=0
        right_count_=0
        for u,v in ranges:
            if (left>=u and left<=v):
                left=v
            if (right>=u and right<=v):
                right=u
            if (right>=u and right<=v) and (left>=u and left<=v):return True
        return False

sol=Solution()
ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5

print(sol.isCovered(ranges,left,right))