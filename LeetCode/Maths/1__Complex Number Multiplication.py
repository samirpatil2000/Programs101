class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b=int(num1.split('+')[0]),int(num1.split('+')[1][:-1])
        c,d=int(num2.split('+')[0]),int(num2.split('+')[1][:-1])
        # print(a,b,c,d)
        return f"{(a*c-b*d)}+{(a*d+b*c)}i"
sol=Solution()
num1 = "1+1i"
num2 = "1+1i"

num1 = "1+-1i"
num2 = "1+-1i"
print(sol.complexNumberMultiply(num1,num2))