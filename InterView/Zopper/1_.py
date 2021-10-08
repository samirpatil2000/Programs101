"""
1. Efficiently calculate the frequency of all elements present in a limited range array
        Given an unsorted integer array whose elements lie in the range 0 to n-1 where n is the array size, 
calculate the frequency of all array elements in linear time using constant space
For example,
    Input: { 2, 3, 3, 2, 1 }
    Output: Element 1 appears once.
    Element 2 appears twice. Element 3 appears twice."""


from typing import List


def findOccurence(arr:List[int])->List[int]:
    n=len(arr)
    for i in range(n):
        arr[arr[i]%n]+=n
    for i in range(n):
        arr[i]=arr[i]//n
        if arr[i]!=0:
            if i==1:
                print("Element "+str(i)+" appears once")
            elif i==2:
                print("Element "+str(i)+" appears twice")
            elif i==3:
                print("Element "+str(i)+" appears thrice")
            else:
                print("Element "+str(i)+" appears "+str(i))
    return arr 
                
def findOccurence_2(arr:List[int])->List[int]:
    result=[]
    for i in range(len(arr)):
        if arr[i]<0:
            result.append(i)
        arr[abs(arr[i])]=-arr[abs(arr[i])]
    print(arr)
    return result
    


        
    return arr
arr=[2,2,3,3,3,1]
print(findOccurence(arr))
print(findOccurence_2(arr)
)        
    