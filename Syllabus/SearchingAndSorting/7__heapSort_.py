from typing import List


class Solution:
    def heapSort(self,arr:List[int])->List[int]:
        def heapify(arr:List[int],n:int,i:int):
            largest=i
            left=2*i+1
            right=2*i+2
            if left<n and arr[left]>arr[largest]:
                largest=left
            if right<n and arr[right]>arr[largest]:
                largest=right
            
            if largest!=i:
                arr[i],arr[largest]=arr[largest],arr[i]
                heapify(arr,n,largest)
                
                
        
        for i in range(len(arr)//2-1,-1,-1):
            heapify(arr,len(arr),i)
        print(arr)
        for i in range(len(arr)-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i]
            print(arr,i)
            heapify(arr,i,0)
            print(arr)    