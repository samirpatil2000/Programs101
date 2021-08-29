from typing import List


class Solution:
    def countOnes(self,n):
        count_=0
        while n>0:
            rsbm=n&(-n)
            n-=rsbm
            count_+=1
        return count_
    
sol=Solution()
print(sol.countOnes(2334566755342))
        