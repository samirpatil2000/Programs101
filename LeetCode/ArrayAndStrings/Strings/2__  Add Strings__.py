class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1,n2=len(num1)-1,len(num2)-1
        carry,ans,idx=0,0,1
        while n1>=0 and n2>=0:
            sum_=int(num1[n1])+int(num2[n2])+carry
            carry=sum_//10
            ans+=((sum_%10)*idx)
            idx*=10
            n1-=1
            n2-=1
            print(ans,carry,idx)
        while n1>=0:
            sum_=int(num1[n1])+carry
            carry=sum_//10
            ans+=((sum_%10)*idx)
            idx*=10
            n1-=1
        while n2>=0:
            sum_=int(num2[n2])+carry
            carry=sum_//10
            ans+=((sum_%10)*idx)
            idx*=10
            n2-=1
        if carry:
            ans+=carry*idx
        return ans
        

sol=Solution()
num1="11"
num2="999"
print(sol.addStrings(num1,num2))        

# result=["0"]*max(n1,n2)
# for i in range(min(n1,n2)):
#     temp=int(num1[i])+int(num2[i])+int(result[i]) #12
#     temp=str(temp)
#     print(temp,i)

#     result[i]=temp[-1]
#     if len(temp)>1:
#         result[i+1]=temp[0]
# return ''.join(result)