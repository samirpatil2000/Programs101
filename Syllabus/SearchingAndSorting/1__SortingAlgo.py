from typing import List


class Solution:
    #                    Best    Average     Worst
    # Time Complexity:  O(n^2)   O(n^2)      O(n^2)
    # Space Complexity: O(1)      O(1)        O(1)
    
    def bubbleSort(self,arr:List[int])->List[int]:
        count_=0
        for i in range(len(arr)):
            for j in range(len(arr)-1):
                print(arr[j],arr[j+1],arr[j+1]<arr[j])
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                count_+=1
                    
        print(count_)
    
    #                    Best    Average     Worst
    # Time Complexity:  O(n^2)   O(n^2)      O(n^2)
    # Space Complexity: O(1)      O(1)        O(1)
    def selectionSort(self,arr:List[int])->List[int]:
        count=0
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
                count+=1
            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(count,len(arr))
            
            
    #                    Best:               Average  Worst: 
    #                    sorted and reverse            arr is sorted     
    # Time Complexity:   O(n)     <O(n^2)      O(n^2)      
    # Space Complexity:  O(1)      O(1)        O(1)
    def insertionSort(self,arr:List[int])->List[int]:
        count_=0
        for i in range(1, len(arr)):
            j = i-1
            key = arr[i]
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
                count_+=1
            arr[j+1] = key
        print(count_,len(arr))   
        
    def mergeSort(self,arr:List[int])->List[int]:
        self.mergeSortHelper(arr, 0, len(arr)-1)
        return arr         
    def mergeSortHelper(self,arr:List[int],left:int,right:int)->List[int]:
        
        def merge(Arr:List[int], start:int, mid:int, end:int)->None:
            temp = [0] * (end - start + 1)

            # crawlers for both intervals and for temp
            i, j, k = start, mid+1, 0

            # traverse both lists and in each iteration add smaller of both elements in temp 
            while(i <= mid and j <= end) :
                if(Arr[i] <= Arr[j]) :
                    temp[k] = Arr[i]
                    k += 1; i += 1
                else :
                    temp[k] = Arr[j]
                    k += 1; j += 1

            # add elements left in the first interval 
            while(i <= mid) :
                temp[k] = Arr[i]
                k += 1; i += 1

            # add elements left in the second interval 
            while(j <= end) :
                temp[k] = Arr[j]
                k += 1; j += 1

            # copy temp to original interval
            for i in range (start, end+1) :
                Arr[i] = temp[i - start]
            
        if left<right:
            mid=(left+right)//2
            self.mergeSortHelper(arr, left, mid)
            self.mergeSortHelper(arr, mid+1, right)
            merge(arr, left, mid, right)
            
    
    def quickSort(self,arr:List[int])->List[int]:
        def partition(arr,left,right)->int:
            
            
        
        
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
    
            
                        
                    
sol=Solution()
arr=[1,4,2,5,3,8,7]

# i=0
# while i<200:
#     arr+=[1,4,2,5,3]
#     i+=1
    
# arr=[1,2,3,4,5]
# arr=[5,4,3,2,1]
# arr.sort()
print(sol.heapSort(arr))
print(arr)
