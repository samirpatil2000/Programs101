from typing import List


class Solution:
    
    def prev_next_min_element(self,arr:List[int])->List[int]:
        n=len(arr)
        next_min=[n]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and arr[i]<=arr[st[-1]]:
                st.pop()
            if st:
                next_min[i]=st[-1]
            st.append(i)
        st.clear()
        
        prev_min=[-1]*n
        for i in range(n):
            while st and arr[i]<=arr[st[-1]]:
                st.pop()
            if st:
                prev_min[i]=st[-1]
            st.append(i)
        return zip(prev_min,next_min)
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        x=self.prev_next_min_element(heights)
        max_=-2**32
        i=0
        for u,v in x:
            max_=max((v-u-1)*heights[i],max_)
            i+=1
        return max_
        
        
sol=Solution()
heights = [2,1,5,6,2,3]
print(sol.largestRectangleArea(heights))