from typing import List


class Solution:
    def minY(self,trees:List[List[int]]):
        y=trees[0]
        for i in trees:
            if i[1]<y[1]:
                y=i
        return y
    def cross(a:List[int],b:List[int],c:List[int]):
        area=(c[1]-b[1])*(b[0]-a[0])-(b[1]-a[1])*(c[0]-b[0])
        return area/abs(area)
    def slope(b:List[int],o:List[int]):
        m=(o[1]-b[1])//(o[0]-b[0])
        return m
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        min_of_y=self.minY(trees)
        print(min_of_y)
        sorted_point=sorted(trees,key=self.slope(min_of_y))
        print(sorted_point)
        
sol=Solution()
points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
print(sol.outerTrees(points))