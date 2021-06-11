from typing import List
import heapq

class Solution:
    
    def maxResult(self, nums: List[int], k: int) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]

        for i in range(1,len(nums)):
            max_=-2**32
            for j in range(i-1,max(i-k-1,-1),-1):
                max_=max(dp[j]+nums[i],max_)
            dp[i]=max_
        return dp
    
    #using heap optimal
    def maxResultOpt(self, nums: List[int], k: int) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        queue=[[-dp[0],0]]
        heapq.heapify(queue)
        for i in range(1,len(nums)):
            # print(queue)
            while queue:
                x=queue[0]
                print(x,i)
                if (x[1] and x[1]>=k):
                    heapq.heappop(queue)
                
                    
                # heapq.heappush(queue,x)
                                
            
            heapq.heappush(queue,[-dp[i],i])
        return dp
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = deque()
        deq.append(0)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + dp[deq[0]]     #Maximum Value in deque within that window
            if deq[0] < i - k + 1:
                deq.popleft()                #Check whether left bound is still accessible or not
            while deq and dp[deq[-1]] < dp[i]:         
                deq.pop()                    #Update deque with current i'th element
            deq.append(i)
        return dp[-1]                        #Return total score
    
    

sol=Solution()
nums = [1,-5,-20,4,-1,3,-6,-3]
k = 2
print(sol.maxResult(nums,k))
print(sol.maxResultOpt(nums,k))
        
        
        
        