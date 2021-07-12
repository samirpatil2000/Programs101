import heapq
from typing import List
class MedianFinder:
    
    def __init__(self):
        self.maxHeap=[]
        self.minHeap=[]
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)
        
        

    def addNum(self, num: int) -> None:
        top_maxHeap=None
        if self.maxHeap:
            top_maxHeap= -heapq.heappop(self.maxHeap)
            print(top_maxHeap,num)
        if len(self.maxHeap)==0 or top_maxHeap>=num:
            if top_maxHeap or top_maxHeap==0:
                heapq.heappush(self.maxHeap,-top_maxHeap)
            heapq.heappush(self.maxHeap,-num)
        else:
            heapq.heappush(self.minHeap,num)
        # self.Balance()
    
    def findMedian(self) -> float:
        print(self.maxHeap,self.minHeap)
        if len(self.maxHeap)>len(self.minHeap):
            return -heapq.heappop(self.maxHeap)
        elif len(self.maxHeap)<len(self.minHeap):
            return heapq.heappop(self.minHeap)
        else:
            
            return (-heapq.heappop(self.maxHeap)+heapq.heappop(self.minHeap))/2
    
    def Balance(self):
        if len(self.maxHeap)-len(self.minHeap)>1:
            heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        elif len(self.minHeap)-len(self.maxHeap)>1:
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
        

from heapq import *

class MedianFinder:

    def __init__(self):
        self.min_heap: List[int] = []
        self.max_heap: List[int] = []
        

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -heappushpop(self.min_heap, num))
        
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        

    def findMedian(self) -> float:
        has_even_count = len(self.max_heap) == len(self.min_heap)
        if has_even_count:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return float(self.min_heap[0])           


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
# obj.addNum(4)
print(obj.minHeap,obj.maxHeap)
# print(obj.findMedian())

