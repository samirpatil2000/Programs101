class Solution:
    def countPalidromicSubstrings(self, s):
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        count=0
        for gap in range(n):
            # traverse from diagonals
            row=0
            col=gap
            
            while col<n:
                if gap==0:
                    dp[row][col]=True
                elif gap==1:
                    dp[row][col]= s[row]==s[col]
                    # if s[row]==s[col]:
                    #     dp[row][col]=True
                    # else:
                    #     dp[row][col]=False
                else:
                    if s[row]==s[col] and dp[row+1][col-1]==True:
                        dp[row][col]=True
                    else:
                        dp[row][col]=False
                
                if dp[row][col]==True:
                    count+=1
                row+=1
                col+=1
        return count
    
sol=Solution()
s="abccbc"
print(sol.countPalidromicSubstrings(s))
                    
                
                    