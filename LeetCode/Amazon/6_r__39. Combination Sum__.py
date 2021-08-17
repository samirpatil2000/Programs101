from typing import List


x=[[1],[3]]

                
                
# x=[i+[2] for i in x]
# print(x)

class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        if target==0:
            return [[]]
        elif target<0:
            return None
        result=[]
        for i in range(len(arr)):
            x=self.combinationSum(arr[i:],target-arr[i])
            if x!=None:
                result+=[l+[arr[i]] for l in x]
        return result        
    
    
sol=Solution()
arr = [2,3,6,7]
target = 7

arr = [2,3,5]
target = 8
print(sol.combinationSum(arr,target))

# print(arr[0:])