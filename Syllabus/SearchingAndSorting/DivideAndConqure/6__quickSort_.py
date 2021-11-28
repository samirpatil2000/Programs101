from typing import List


class Solution:
    
    def partitions(self,arr:List[int],low:int,high:int):
        pivot=arr[low]
        start=low
        end=high
        while start<end:
            while arr[start]<=pivot:
                start+=1
            while arr[end]>pivot:
                end-=1
            if start<end:
                arr[end],arr[start]=arr[start],arr[end]
            arr[low],arr[end]=arr[end],arr[low]
        return end
    
    def quickSort(self,arr:List[int],low:int,high:int):
        if low<high:
            part=self.partitions(arr,low,high)
            self.quickSort(arr,low,part-1)
            self.quickSort(arr,part+1,high)
        

sol=Solution()
arr=[2,5,4,6,2,9,8,10,16,15]
print(sol.partitions(arr,0,len(arr)-1))
print(arr)
        

        
    
            

sol=Solution()
