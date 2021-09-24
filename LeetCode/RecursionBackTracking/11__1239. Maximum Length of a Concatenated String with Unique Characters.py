from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n=len(arr)
        if n==1:
            return len(arr[0])
        max_=[0]
        def dfs(index,psf):
            if len(psf)!=len(set(psf)):
                return
            max_[0]=max(max_[0],len(psf))
            for i in range(index,n):
                dfs(i+1,psf+arr[i])
        dfs(0,"")
        return max_[0]
    
    #DP SOLUTION
    def maxLength_II(self,arr:List[str]):
        dp = ['']
        res = 0
        for i in range(len(arr)):
            for j in range(len(dp)):
                local = arr[i]+dp[j]
                if len(local)==len(set(local)):
                    dp.append(local)
                    res=max(res,len(local))
        return res
        
        
            
sol=Solution()
arr=["un","iq","ue"]
# arr=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
# arr = ["cha","r","act","ers"]
# arr = ["abcdefghijklmnopqrstuvwxyz"]
# arr=["yy","bkhwmpbiisbldzknpm"]
arr=["a", "abc", "d", "de", "def"]
print(sol.maxLength(arr))            