from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n==1:
            return [1]
        
        arr=[1,2]
        for _ in range(n+1):
            even_arr=[]
            for i in arr:
                if 2*i<=n:
                    even_arr.append(2*i)

            odd_arr=[]
            for i in arr:
                if 2*i-1<=n: 
                    odd_arr.append(2*i-1)
            arr=odd_arr+even_arr
        return arr
sol=Solution()
print(sol.beautifulArray(5))                
            
        
        