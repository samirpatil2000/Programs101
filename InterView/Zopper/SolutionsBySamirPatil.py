


from typing import List
# Solutions by Samir Patil

class Question1:
    def findOccurence(self,arr:List[int])->List[int]:
        n=len(arr)
        for i in range(n):
            arr[arr[i]%n]+=n
        for i in range(n):
            arr[i]=arr[i]//n
            if arr[i]!=0:
                if arr[i]==1:
                    print("Element "+str(i)+" appears once.")
                elif arr[i]==2:
                    print("Element "+str(i)+" appears twice.")
                elif arr[i]==3:
                    print("Element "+str(i)+" appears thrice.")
                else:
                    print("Element "+str(i)+" appears "+str(arr[i])+" times.")
                    
class Question2:
    def maxSumNonCircularSubArr(self,arr:List[int])->int:
        n=len(arr)
        max_=-2**32
        current_sum=0
        for i in range(n):
            current_sum+=arr[i]
            max_=max(current_sum,max_)
            if current_sum<0:
                current_sum=0
        return max_

    def maxSumCircularSubArr(self,arr:List[int])->int:
        maxSubArrayInNonCircular=self.maxSumNonCircularSubArr(arr)
        total_sum=0
        for i in range(len(arr)):
            total_sum+=arr[i]
            arr[i]=-arr[i]
        res=max(maxSubArrayInNonCircular,total_sum+self.maxSumNonCircularSubArr(arr))
        if res:return res
        return -min(arr)
        



"""
1. Efficiently calculate the frequency of all elements present in a limited range array
    Given an unsorted integer array whose elements lie in the range 0 to n-1 where n is the array size, 
    calculate the frequency of all array elements in linear time using constant space
"""

Q1=Question1()
arr=[2, 3, 3, 2, 1,0,0,0,0]
Q1.findOccurence(arr)


"""
2. Maximum Sum Circular Subarray
Given a circular integer array, find a subarray with the largest sum in it.

"""
Q2=Question2()
arr=[2, 1, -5, 4, -3, 1, -3, 4, -1]
print(Q2.maxSumCircularSubArr(arr))


        
    