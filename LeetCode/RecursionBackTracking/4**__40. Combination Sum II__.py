from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def rec_(index,arr,target,sumSoFar):
            
            if target<0:
                return
            if target==0:
                # print(sumSoFar)
                result.append(sumSoFar)
                return
            for i in range(index,len(arr)):
                if i>index and arr[i]==arr[i-1]:continue # think for this
                if target>=arr[i]:
                    rec_(i+1,arr,target-arr[i],sumSoFar+[arr[i]])
            return 
        rec_(0,candidates,target,[])
        return result
    
sol=Solution()
candidates = [10,1,2,7,6,5]
target = 8
print(sol.combinationSum2(sorted(candidates),target))
            