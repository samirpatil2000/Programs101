import math
from typing import List, Set


class Solution:
    def __init__(self, destination: List[int], stations: List[List[int]]) -> None:
        
        self.dest = destination
        self.stations    =  stations
    
    def calculate_distance(self, dest: List[int], curr: List[int]):
        return math.sqrt(sum([(dest[i] - curr[i])**2 for i in range(3)]))
        
    def keyFun(self, curr: List[int]):
        return math.sqrt(sum([(self.dest[i] - curr[i])**2 for i in range(3)]))
        
        
    def subtraction(self, x, y):
        return [x[i] - y[i] for i in range(3)]
        
    def findPlanet(self):
        
        self.stations.sort(key=self.keyFun)
        print(self.stations)
        def dfs(dest: List[int], index = 0):
            print(dest)
            if index == len(self.stations) - 1:
                return -1
            if dest[0] == dest[1] == dest[2] == 0:
                return 0
            min_ = 2**32
            for i in range(index, len(self.stations)):
                x = dfs(self.subtraction(dest, self.stations[i]), i + 1)
                if x != -1:
                    min_ = min(x + self.calculate_distance(self.stations[i], dest), min_)
            if min_ == 2**32:
                return -1
            return min_
        
        return dfs(self.dest)
                    
                
            
            
            
        

destination = (2, 2, 2)
stations = [(0, 0, 2), (0, 2, 2), (2, 0, 0)]
stations = [(1, 1, 1), (1, 2, 2), (2, 1, 1)]

sol = Solution(destination, stations)
print(sol.findPlanet())