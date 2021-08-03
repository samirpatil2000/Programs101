class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        count_=0
        for gap in range(0,n):
            row=0
            col=gap
            while col<n:
                if gap==0:
                    dp[row][col]=True
                elif gap==1:
                    dp[row][col]= s[row]==s[col]
                        
                else:
                    if dp[row+1][col-1]==True and s[row]==s[col]:
                        dp[row][col]=True
                if dp[row][col]:
                    count_+=1
                col+=1
                row+=1
                
        return count_
    
    
sol=Solution()
print(sol.countSubstrings(s="abc"))
print(sol.countSubstrings(s="aaa"))
    
    