class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i=0
        ans=0
        while i<n:
            ans=ans^(start+2*i)
            i+=1
        return ans
    
    
sol=Solution()
n = 5
start = 0
print(sol.xorOperation(n,start))

x=0 ^ 2 ^ 4 ^ 6 ^ 8
print(x)