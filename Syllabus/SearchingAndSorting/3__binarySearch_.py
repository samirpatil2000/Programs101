
from typing import List


class Solution:
    def binarySearch(self,arr:List[int],target:int):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left if arr[left] == target else -1
    
        
sol=Solution()
print(sol.binarySearch([2,3,4,5],3))