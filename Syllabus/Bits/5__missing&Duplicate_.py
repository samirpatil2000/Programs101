from typing import List


class Solution:
    def missingAndDuplicate(self,arr:List[int],n:int):
        x_xor_y=0
        for val in arr:x_xor_y^=val
        for val in range(1,n+1):x_xor_y^=val
        x,y=0,0
        rmsbt=x_xor_y&(-x_xor_y)
        for val in arr:
            if rmsbt&val==0:x^=val
            else:y^=val
        for val in range(1,n+1):
            if rmsbt&val==0:x^=val
            else:y^=val
        for val in arr:
            if x==val:
                return f"Repeating {x},Missing {y}"
            elif y==val:
                return f"Repeating {y},Missing {x}"
                
sol=Solution()
arr=[3,6,2,5,1,2,7]
print(sol.missingAndDuplicate(arr,7))