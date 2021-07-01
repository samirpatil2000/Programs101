from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        distribution=[1]*n
        
        for i in range(n-1):
            if ratings[i+1]>ratings[i]:
                distribution[i+1]=distribution[i]+1

        
        for i in range(n-1,0,-1):
            if ratings[i-1]>ratings[i]:
                if distribution[i-1]<=distribution[i]:
                    distribution[i-1]=distribution[i]+1
        return sum(distribution)
    
sol=Solution()
ratings = [1,0,2]
print(sol.candy(ratings))
                