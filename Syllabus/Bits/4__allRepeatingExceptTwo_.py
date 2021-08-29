from typing import List


class Solution:
    def all_repeating_except_two(self,arr:List[int]):
        x_xor_y=0
        for val in arr:
            x_xor_y=x_xor_y^val
        rmsbt=x_xor_y&(-x_xor_y)
        x,y=0,0
        for val in arr:
            if rmsbt&val==0:
                x=x^val
            else:
                y=y^val
        return min(x,y),max(x,y)
            
sol=Solution()
arr=[24,56,42,24,50,50]
print(sol.all_repeating_except_two(arr))
        
        