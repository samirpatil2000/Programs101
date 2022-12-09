from typing import List

import time
class Solution:
    def rank_array(self, arr:List[int]):
        import heapq
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, [arr[i], i])
        result = []
        for i in range(len(arr)):
            val, idx = heapq.heappop(heap)
            arr[idx] = i + 1
        # i = 0
        # while heap:
        #     val, idx = heapq.heappop(heap)
        #     arr[idx] = i + 1
        #     i += 1
        return 2
    

arr = [22, 11, 44, 66, 55]
arr = [15, 12, 11, 10, 9]
t1 = time.time()

print(Solution().rank_array(arr * 10000))
print("Total Time: ", time.time() - t1)