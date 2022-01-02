from typing import List


class Solution:
    def numPairsDivisibleBy60(self, arr: List[int]) -> int:
        Hash=[0]*60
        for ele in arr:
            Hash[ele%60]+=1
        
        result=0
        for i in range(1,30):
            result+=(Hash[i]*Hash[60-i])
        #kC2 => k*(k-1)/2
        if Hash[0]>0:
            result+=Hash[0]*(Hash[0]-1)//2
        if Hash[30]>0:
            result+=Hash[30]*(Hash[30]-1)//2
        return result
    
    
sol=Solution()
arr=[15,63,451,213,37,209,343,319]
# arr=[439,407,197,191,291,486,30,307,11]
# arr=[60,60,60]
print(sol.numPairsDivisibleBy60(arr))
