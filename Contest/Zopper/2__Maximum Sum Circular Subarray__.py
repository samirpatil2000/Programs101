
"""
2. Maximum Sum Circular Subarray
Given a circular integer array, find a subarray with the largest sum in it.
For example,
    Input: { 2, 1, -5, 4, -3, 1, -3, 4, -1}
    Output: Subarray with the largest sum is {4, -1, 2,1} with sum 6.
    Input: {-3, 1, -3, 4, -1, 2, 1, -5, 4}
    Output: Subarray with the largest sum is {4, -1, 2, 1} with sum 6.
"""


from typing import List

def maxSumNonCircularArr(arr:List[int])->int:
    n=len(arr)
    max_=-2**32
    current_sum=0
    for i in range(n):
        current_sum+=arr[i]
        max_=max(current_sum,max_)
        if current_sum<0:
            current_sum=0
    return max_


def maxSumForCircularArr(arr:List[int])->int:
    maxSubArrayInNonCircular=maxSumNonCircularArr(arr)
    total_sum=0
    for i in range(len(arr)):
        total_sum+=arr[i]
        arr[i]=-arr[i]
    res=max(maxSubArrayInNonCircular,total_sum+maxSumNonCircularArr(arr))
    if res:
        return res
    return -min(arr)

arr=[2, 1, -5, 4, -3, 1, -3, 4, -1]
# Solution by Samir Patil
print(maxSumForCircularArr(arr))
        

