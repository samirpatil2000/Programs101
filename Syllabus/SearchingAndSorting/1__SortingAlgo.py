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
        

            
        
        
                
    
    def shellSort(self,arr:List[int])->List[int]:
        n=len(arr)
        gap=n/2
        while gap>0:
            left=0
            right=gap
            
            while right<n:
                if arr[left]>arr[right]:
                    arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right+=1
                
                extrem_left=left
                while extrem_left-gap>=0:
                    if arr[extrem_left-gap]>arr[extrem_left]:
                        arr[extrem_left-gap],arr[extrem_left]=arr[extrem_left],arr[extrem_left-gap]
                    extrem_left-=1                                
                    
                    
                    
        
            
                        
                    
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
