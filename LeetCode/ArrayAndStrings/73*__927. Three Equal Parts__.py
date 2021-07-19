from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total_one_count=sum(arr)
        if total_one_count==0:
            return [0,2]
        
        numOf1sInEachPart = total_one_count // 3
        if total_one_count%3!=0:
            return [-1,-1]
        f1,s1,t1 = [-1]*3
        one_count=0
        for i in range(len(arr)):
            if arr[i]==1:
                one_count+=1
                if one_count==1:
                    f1=i
                elif one_count==(numOf1sInEachPart+1):
                    s1=i
                elif one_count==(2*numOf1sInEachPart+1):
                    t1=i
        while t1<len(arr):
            if arr[f1]==arr[s1] and arr[s1]==arr[t1]:
                f1+=1
                s1+=1
                t1+=1
            else:
                return [-1,-1]
        return [f1-1,s1]
    
    def sol2(self,arr):
        ans = [-1, -1]
        numOf1s = 0
        n = len(arr)
        for i in range(n):
            numOf1s += arr[i]
        
        if numOf1s % 3 != 0:
            return ans
        
        if numOf1s == 0:
            return [0, 2]
        
        numOf1sInEachPart = numOf1s // 3
        numOf1s = 0
        firstPart1, secondPart1, thirdPart1 = -1, -1, -1
        for i in range(n):
            if arr[i] == 1:
                numOf1s += 1
                if numOf1s == 1:
                    firstPart1 = i
                
                elif numOf1s == (numOf1sInEachPart + 1):
                    secondPart1 = i
                
                elif numOf1s == (2 * numOf1sInEachPart + 1):
                    thirdPart1 = i
        
        while thirdPart1 < n:
            if arr[thirdPart1] == arr[firstPart1] and arr[secondPart1] == arr[thirdPart1]:
                firstPart1 += 1
                secondPart1 += 1
                thirdPart1 += 1
            
            else:
                return ans
            
        
        return [firstPart1 - 1, secondPart1]
        
        
sol=Solution()
arr = [1,0,1,0,1]
arr=[1,1,1,1,1,1,0,1,1,1]
print(sol.threeEqualParts(arr))                   
print(sol.sol2(arr))                   
                
                
        
        