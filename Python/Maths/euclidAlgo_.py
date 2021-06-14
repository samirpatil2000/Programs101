
from typing import List
import math

class Solution:
    def gcd(self,a:int,b:int) -> int:
        if b==0:return a
        print(a,b)
        return self.gcd(b,a%b)
    
sol=Solution()
gcd_=sol.gcd(12,2499322)

print(gcd_)   
print(45%50,45//50)   
        