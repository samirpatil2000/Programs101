from typing import List


class Solution:
    def printAllPaths(self, jumps:List[int]):
        n = len(jumps)
        dp=[0]*(n)
        dp[-1]=0
        for i in range(n-2,-1,-1):
            min_=2**31-1
            for j in range(1,jumps[i]+1):
                if j+i>=n:break
                min_=min(min_,dp[i+j])
            dp[i]=min_+1
        print(dp)
        q=[[0,""]]
        while q:
            curr_index,psf=q.pop(0)
            print(curr_index,psf)
            if curr_index==n-1:
                print(psf)
                return
            min_step=dp[curr_index]-1
            for i in range(1,jumps[curr_index]+1):
                if i+curr_index >=n:break
                if dp[curr_index+i]==min_step:
                    q.append([i+curr_index,psf+str(i+curr_index)])
        return None
    
sol=Solution()
jumps=[3,3,0,2,1,2,4,2,0,0]
sol.printAllPaths(jumps)
                    
        

    
