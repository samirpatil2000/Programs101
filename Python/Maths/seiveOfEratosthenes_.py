from typing import List
import math

class Solution:
    def isPrimeList(self,n:int) -> List[int]:
        arr=[True]*(n+1)
        arr[0]=arr[1]=False
        
        for i in range(2,math.floor(math.sqrt(n))):
            for j in range(2*i,n+1,i):
                arr[j]=False
                
        return arr
    def SieveOfEratosthenes(self,n):
          
        # Create a boolean array "prime[0..n]" and initialize
        # all entries it as true. A value in prime[i] will
        # finally be false if i is Not a prime, else true.
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            # If prime[p] is not changed, then it is a prime
            if (prime[p] == True):                
                # Update all multiples of p
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        prime[0]= False
        prime[1]= False
        return prime
    
sol=Solution()
isPrime=sol.isPrimeList(12)
x=sol.SieveOfEratosthenes(12)
print(isPrime)
print(x)
print(isPrime[9+1])

print(isPrime[11+1])      
        