class Solution:
    
    def findSquareRoot(self,n):
        left=0
        right=n
        eps=1e-6
        while right-left>eps:
            mid=(left+right)/2
            
            if mid*mid<n:
                left=mid
            else:
                right=mid
        
        return round(left,5),round(right,5)

sol=Solution()
n=2
print(sol.findSquareRoot(n))