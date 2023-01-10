import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        heap = [[nums[i] * -1, i] for i in range(k)]
        heapq.heapify(heap)
        result = [heap[0][0] * -1]
        for i in range(k, len(nums)):
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            heapq.heappush(heap, [nums[i] * -1, i])
            result.append(heap[0][0] * -1)
        return result


nums = [1, 3,-1,-3,5,3,6,7]
k = 3
# nums = [1,-1]
nums = [9,10,9,-7,-4,-8,2,-6]
k = 5
print(Solution().maxSlidingWindow(nums, k))

[3,3,5,5,6,7] # Ans


[3, 5, 5, 6, 7, 7]

# [10,10,9,2]