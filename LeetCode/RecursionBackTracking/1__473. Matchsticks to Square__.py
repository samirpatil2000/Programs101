from typing import List

# if index>=len(matchsticks):return
#             side_1[0]=side_1[0]+matchsticks[index]
#             dfs(index+1)
#             dfs(side_1,side_2[0]+matchsticks[index],side_3,side_4,index+1)
#             dfs(side_1,side_2,side_3[0]+matchsticks[index],side_4,index+1)
#             dfs(side_1,side_2,side_3,side_4[0]+matchsticks[index],index+1)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks)<4:return False
        sum_=sum(matchsticks)
        if sum_%4!=0:
            print("x")
            return False
        perimeter=sum_//4
        side_arr=[perimeter]*4
        if max(matchsticks) > perimeter:
            return False
        
        def dfs(side_arr,index=0):
            print(side_arr,matchsticks[index])
            if index==len(matchsticks):
                if side_arr[0]==0 and side_arr[1]==0 and side_arr[2]==0 and side_arr[3]==0:
                    return True
                else:
                    return False
            for i in range(4):
                if matchsticks[index]>side_arr[i]:
                    continue
                side_arr[i]-=matchsticks[index]
                if dfs(side_arr,index+1):
                    return True
                side_arr[i]+=matchsticks[index]
            return False
        # return dfs(side_arr)
        
        
        
        arr=[0]*4
        def dfs_optimise(matchSticks,arr):
            print(arr)
            if any(side > perimeter for side in arr):
                return False
            elif not matchSticks and all(side==perimeter for side in arr):
                return True
            else:
                return (
                    dfs_optimise(matchSticks[1:],[arr[0]+matchSticks[0],arr[1],arr[2],arr[3]]) or
                    dfs_optimise(matchSticks[1:],[arr[0],arr[1]+matchSticks[0],arr[2],arr[3]]) or
                    dfs_optimise(matchSticks[1:],[arr[0],arr[1],arr[2]+matchSticks[0],arr[3]]) or
                    dfs_optimise(matchSticks[1:],[arr[0],arr[1],arr[2],arr[3]+matchSticks[0]])
                    )
                
        return dfs_optimise(sorted(matchsticks, reverse=True),arr)
            
sol=Solution()
matchsticks = [1,1,2,2,2]
matchsticks = [3,3,3,3,4]
matchsticks = [1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755]
print(sol.makesquare(matchsticks))
            