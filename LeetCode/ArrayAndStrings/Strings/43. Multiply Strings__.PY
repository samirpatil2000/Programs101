class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        e1=0
        ans=0
        for e1,n1 in enumerate(num2[::-1]):
            res=0
            for e2,n2 in enumerate(num1[::-1]):
                res+=((int(n1)*int(n2))*10**e2)
            ans+=(res*10**e1)
        return str(ans)


sol=Solution()
num1 = "123"
num2 = "456"
print(sol.multiply(num1,num2))