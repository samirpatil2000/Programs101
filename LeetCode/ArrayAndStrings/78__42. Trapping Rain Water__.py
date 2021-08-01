from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_max=[-1]*n
        right_max=[-1]*n
        left_max_el=0
        for i in range(1,n):
            left_max_el=max(left_max_el,height[i-1])
            left_max[i]=left_max_el
        right_max_el=0
        for i in range(n-2,-1,-1):        
            right_max_el=max(right_max_el,height[i+1])
            right_max[i]=right_max_el
        water=0
        for i in range(1,n-1):
            x=min(left_max[i],right_max[i])-height[i]
            if x>0:
                water+=x
        return water
sol=Solution()
heights=[0,1,0,2,1,0,1,3,2,1,2,1]
# heights=[2,1,0,2]
# heights=[4,2,0,3,2,5]
print(sol.trap(heights))