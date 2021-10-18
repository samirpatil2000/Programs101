from typing import List


class Solution:
    def getMax(self,arr,partition):
        if partition==0:
            return -2**32
        return arr[partition-1]
    
    def getMin(self,arr,partition):
        if partition==len(arr):
            return 2**32
        return arr[partition]
        
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        if len(A)>len(B):
            A,B=B,A
        left=0
        right=len(A)
        total_len=len(A)+len(B)
        
        while left<=right:
            a_left=(left+right)//2
            b_left=(total_len+1)//2-a_left
            
            leftX=self.getMax(A,a_left)
            rightX=self.getMin(A,a_left)
            
            leftY=self.getMax(B,b_left)
            rightY=self.getMin(B,b_left)
            
            if leftX<=rightY and leftY<=rightX:
                
                if total_len&1!=1: #even
                    return (max(leftX,leftY)+min(rightY,rightX))/2
                else:
                    return max(leftX,leftY)
                
            elif leftX>rightY:
                right=a_left-1
            elif leftY>rightX:
                left=a_left+1
        return -1
    

sol=Solution()
A=[ 0, 23 ]
B=[  ]

print(sol.findMedianSortedArrays(A,B))