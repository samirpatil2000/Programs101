class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=1
        b=int(c**(0.5))
        if b*b==c:
            return True,(a,b)
        while a<=b:
            sum_=a*a+b*b
            if sum_==c:
                return True,(a,b)
            else:
                if sum_<c:
                    a+=1
                else:
                    b-=1
        return False
                    
        

sol=Solution()
c=7
c=6
c=5
# c=4
# c=3
# c=2
# c=1
print(sol.judgeSquareSum(c))