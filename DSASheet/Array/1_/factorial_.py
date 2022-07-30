class Solution:
    def fact(self,n:int):
        if n==1 or n==0:
            return 1
        return n*self.fact(n-1)
sol=Solution()
n=48
x=sol.fact(n)
print(len(str(x)))
print(-1e6)
