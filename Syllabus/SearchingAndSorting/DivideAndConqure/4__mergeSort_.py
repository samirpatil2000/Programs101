from typing import List


class Solution:
    
    def merge(self,arr:List[int],left:int,mid:int,right:int):
        i = left
        j = mid + 1
        temp = []
        while i <= mid and j <= right:
            if arr[i]< = arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        for j,i in enumerate(range(left,right+1)):
            arr[i] = temp[j]

        
    def mergeSort(self,arr:List[int],left:int,right:int):
        if left<right:
            mid=(left+right)//2
            self.mergeSort(arr,left,mid)
            self.mergeSort(arr,mid+1,right)
            self.merge(arr,left,mid,right)
            

sol=Solution()
arr=[-1,-2,3]
print(sol.mergeSort(arr,0,len(arr)-1))
print(arr)