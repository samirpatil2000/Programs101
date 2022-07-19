from audioop import reverse
from typing import List


class Solution:
    def reverse(self, arr, start):
        end = len(arr) - 1
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(arr) - 2
        while(i >= 0 and arr[i] >= arr[i+1]):
            i -= 1
        if i == -1:
            self.reverse(arr, 0)
        else:
            j = len(arr) - 1
            while (j>=0 and arr[j] <= arr[i]):
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        self.reverse(arr, i + 1)  
        return arr
                    
         
        
sol = Solution()
arr = [1, 3, 2]
arr = [1,2,3]
arr = [2,3,1]
arr = [1, 2, 3, 4, 5]
for _ in range(6):
    print(sol.nextPermutation(arr))
            
        
