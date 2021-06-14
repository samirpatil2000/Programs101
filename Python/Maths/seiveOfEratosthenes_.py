from typing import List
import math

class Solution:
    def isPrimeList(self,n:int) -> List[int]:
        arr=[True]*(n+1)
        arr[0]=arr[1]=False
        
        for i in range(2,int(math.sqrt(n))):
            for j in range(2*i,n+1,i):
                arr[j]=False
                
        return arr
    
sol=Solution()
isPrime=sol.isPrimeList(12)

print(isPrime[11])      
        