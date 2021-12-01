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
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0
        arr=[0]*len(mat[0])
        max_=0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]=='1':
                    arr[col]+=1
                else:
                    arr[col]=0
            max_=max(max_,self.largestRectangleArea(arr))
        return max_
    
    
sol=Solution()
mat = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
mat = [["1"]]
mat=[]
# mat = [["0","0"]]
# mat = [["0"]]
print(sol.maximalRectangle(mat))