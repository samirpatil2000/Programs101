from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def rec_permutation_BottomUp(arr,target,memo={}):
            if target in memo:return memo[target]
            if target==0:return [[]]
            if target<0:return None
            permutaions=[]
            for i in range(len(arr)):
                x=rec_permutation_BottomUp(arr,target-arr[i],memo)
                if x!=None:
                    for list in x:
                        list.append(arr[i])
                        permutaions.append(list)
            return permutaions
        
        permutaions=[]
        def rec_permutation_TopDown(arr,target,sumSoFar):
            if target==0:
                permutaions.append(sumSoFar)
                return
            if target<0:return
            for i in range(len(arr)):rec_permutation_TopDown(arr,target-arr[i],sumSoFar+[arr[i]])
        rec_permutation_TopDown(candidates,target,[])
        permutaions=rec_permutation_BottomUp(candidates,target)
        
        combinations=[]
        def rec_combination_TopDown(arr,index,target,sumSoFar):
            if index>=len(arr):return
            if target==0:
                combinations.append(sumSoFar)
                return
            if target<0:return
            rec_combination_TopDown(arr,index,target-arr[index],sumSoFar+[arr[index]])
            rec_combination_TopDown(arr,index+1,target,sumSoFar)
        rec_combination_TopDown(candidates,0,target,[])
        
        def rec_combination_BottomUp(arr,index,target):
            if index>=len(arr):return None
            if target==0:return [[]]
            if target<0:return None
            result=[]
            current_index=rec_combination_BottomUp(arr,index,target-arr[index])
            next_index=rec_combination_BottomUp(arr,index+1,target)
            if current_index:
                for i in current_index:
                    i.append(arr[index])
                    result.append(i)
            
            if next_index:
                for i in next_index:
                    i.append(arr[index])
                    result.append(i)
            return result
        x=rec_combination_BottomUp(candidates,0,target)
        
        
        
        # return permutaions,combinations,x
        return combinations
    
    
sol=Solution()
candidates = [2,3,6,7]
target = 7
candidates = [2,3,5]
target = 8
candidates = [2]
target = 1
candidates = [1]
target = 1
print(sol.combinationSum(candidates,target))
                
        