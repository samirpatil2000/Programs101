from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=j=0
        n=len(nums)
        max_=0
        while i<n and j<n:
            
            if k>=0 and nums[j]==1:
                max_=max(j-i+1,max_)
            else:
                max_=max(j-i,max_)
            # print("j-i+1 =",j-i+1,
            #       "max_=",max_,
            #       " i =",i,
            #       " j =",j,
            #       " k =",k )

            if nums[j]==0:
                if k>0:
                    k-=1
                    j+=1
                    
                else:
                    
                    i+=1
                    if nums[i-1]==0:
                        k+=1
            else:
                j+=1
        return j-i+1
    def longestOnes2(self, nums: List[int], k: int) -> int:
        i=0
        n=len(nums)
        max_=0
        for j in range(n):            
            if nums[j]==0:
                k-=1
            if k<0:
                
                if nums[i]==0:
                    k+=1
                i+=1
            max_=max(max_,j-i+1)
        return j-i+1,max_,j,i
    def test(self,A,K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1
    

    
    
sol=Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
#     0,1,2,3,4,5,6,7,8
nums=[0,0,1,1,0,0,0,0,0]
k=2

print(sol.longestOnes(nums,k))
print(sol.longestOnes2(nums,k))
print(sol.test(nums,k))