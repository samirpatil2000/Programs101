from typing import List
from math import atan2

class Solution:
    def minY(self,trees:List[List[int]]):
        y=trees[0]
        for i in trees:
            if i[1]<y[1]:
                y=i
        return y
    
    def cross(self,a:List[int],b:List[int],c:List[int]):
        area=(c[1]-b[1])*(b[0]-a[0])-(b[1]-a[1])*(c[0]-b[0])
        return area 
    
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        start = self.minY(points)
        def sort_acc(p):
            # print(atan2(p[1]-start[1], p[0]-start[0]), -p[1], p[0],p)
            return atan2(p[1]-start[1], p[0]-start[0]), -p[1], p[0]
        # points.pop(points.index(start))
        # points.sort(key=sort_acc)
        points = sorted(points, key=lambda p: (p[0], p[1]))
        lower_stack=[]
        for point in points:
            while len(lower_stack)>1 and self.cross(a=lower_stack[-2],b=lower_stack[-1],c=point)<=0:
                lower_stack.pop()
            lower_stack.append(point)
            
        upper_stack=[]
        for point in reversed(points):
            while len(upper_stack)>1 and self.cross(a=upper_stack[-2],b=upper_stack[-1],c=point)<=0:
                upper_stack.pop()
            upper_stack.append(point)
            
        return lower_stack[:-1]+upper_stack[:-1]
            
            
            
        
    
    def testingSort(self,points:List[List[int]]):
        points.sort(key= lambda x:(-x[0],-x[1]))
        return points
        
sol=Solution()
points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# points      = [[1,1],[1,3],[1,2],[2,2],[2,0],[2,4],[3,3],[4,2],[6,0]]
print(sol.outerTrees(points))
# print(sol.testingSort(x))

