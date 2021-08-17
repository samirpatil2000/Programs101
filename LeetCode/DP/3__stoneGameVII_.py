from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        self.diff=0
        def dfs(a:bool,b:bool,a_score:int,b_score:int,nums:List[int],sum_:int):
            if (len(stones)%2==0 and len(nums)==0) or (len(stones)%2!=0 and len(nums)==1):
                self.diff=abs(a_score-b_score)
                # print(self.diff)
                return
            print(nums)
            # print(a,b,a_score,b_score,nums,sum_)
            if b:
                dfs(True,False,a_score,b_score+(sum_-nums[0]),nums[1:],sum_-nums[0])
                dfs(True,False,a_score,b_score+(sum_-nums[-1]) ,nums[:-1],sum_-nums[-1])
            elif a:
                dfs(False,True,a_score+(sum_-nums[0]),b_score,nums[1:],sum_-nums[0])
                dfs(False,True,a_score+(sum_-nums[-1]),b_score,nums[:-1],sum_-nums[-1])
        dfs(True,False,0,0,stones,sum(stones))
        
        return self.diff
sol=Solution()
stones=[5,3,1,4,2]
print(sol.stoneGameVII(stones))
    
