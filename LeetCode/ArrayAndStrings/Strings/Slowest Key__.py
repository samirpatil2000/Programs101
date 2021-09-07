from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keys: str) -> str:
        n=len(releaseTimes)
        index=0
        max_diff=releaseTimes[0]
        for i in range(1,n):
            x=releaseTimes[i]-releaseTimes[i-1]
            print(x)
            if x==max_diff:
                if max(keys[index],keys[i])==keys[i]:
                    index=i
            elif x>max_diff:
                index=i
                max_diff=x
        return keys[index]
    
sol=Solution()
releaseTimes = [9,29,49,50]
keysPressed = "cbcd"
releaseTimes = [12,23,36,46,62]
keysPressed = "spuda"
print(sol.slowestKey(releaseTimes,keysPressed))