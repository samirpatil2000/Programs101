from typing import List
import heapq

class Solution:
    def finMinMax(self, arr: List[int]):
        heap = heapq.heapify(arr)
        return heapq.heap