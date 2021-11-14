from typing import List
from collections import defaultdict

class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        memo=defaultdict(int)
        n=len(arr)
        buy,sell=arr[0],arr[0]
        for i in range(1,n):
            if buy > arr[i]:
                buy=arr[i]
                sell=arr[i]
            else:
                sell=max(sell,arr[i])
            print(buy)
            memo[buy]=max(sell-buy,memo.get(buy,0))
        return sum(memo.values())
    
sol=Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))
