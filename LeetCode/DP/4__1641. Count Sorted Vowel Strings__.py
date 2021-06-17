class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp=[1]*(5+1)
        total_sum=sum(dp)-1
        if n==1:return total_sum
        for i in range(1,n):
            prev_dp=dp.copy()
            to_be_remove=0
            current_total_sum=0
            for j in range(1,5+1):
                dp[j]=total_sum-to_be_remove
                current_total_sum+=dp[j]
                total_sum-=prev_dp[j]
            total_sum=current_total_sum
        return total_sum
sol=Solution()
print(sol.countVowelStrings(5000))
                
            
            