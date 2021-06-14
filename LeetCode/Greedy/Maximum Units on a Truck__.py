from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        result=0
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        while truckSize>0:
            if boxTypes:
                box=boxTypes.pop(0)
                if truckSize>box[0]:
                    result+=(box[0]*box[1])
                    truckSize-=box[0]
                else:
                    result+=(truckSize*box[1])
                    truckSize=0
            else:
                return result
        return result
    
    
sol=Solution()
boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
truckSize = 35
print(sol.maximumUnits(boxTypes,truckSize))