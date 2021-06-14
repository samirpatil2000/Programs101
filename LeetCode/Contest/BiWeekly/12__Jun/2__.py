from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        sum_=sum(chalk)
        while k>sum_:k%=sum_
        while k>=0 and k>=chalk[i]:
            k-=chalk[i]
            i+=1
            print(i,k)
            if i==len(chalk):
                i=0
        return i
sol=Solution()
chalk = [30,76,46,74,34,12,1,82,25,28,63,29,60,76,98,20,40,32,76,26,71]
# chalk = [3,4,1,2]
# k = 25
k = 346237330
print(sol.chalkReplacer(chalk,k))
            