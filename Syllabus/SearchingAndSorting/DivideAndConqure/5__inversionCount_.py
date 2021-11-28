from typing import List


class Solution:
    
    def merge(self,arr:List[int],left:int,mid:int,right:int):
        i=left
        j=mid+1
        temp=[]
        inv_count=0
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
                inv_count+=(mid-i+1)
                
        while i<=mid:
            temp.append(arr[i])
            i+=1
        while j<=right:
            temp.append(arr[j])
            j+=1
        for j,i in enumerate(range(left,right+1)):
            arr[i]=temp[j]
        return inv_count

        
    def mergeSort(self,arr:List[int],left:int,right:int):
        if left<right:
            mid=(left+right)//2
            inv_count=0
            inv_count+=self.mergeSort(arr,left,mid)
            inv_count+=self.mergeSort(arr,mid+1,right)
            inv_count+=self.merge(arr,left,mid,right)
            return inv_count
        return 0
            

sol=Solution()
arr=[3, 1, 2]
arr=[1, 20, 6, 4, 5]
arr=[5,3,1,4,2]
print(sol.mergeSort(arr,0,len(arr)-1))
print(arr)