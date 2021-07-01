class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        def dfs_topDown(s1,s2,out_,memo={}):
            print(out_,s1,s2)
            if len(s1)==0 and len(s2)==0:
                if out_==s3:
                    return True
                return
            # elif len(s1)==0 or len(s2)==0:
            #     return
            if s1:
                if dfs_topDown(s1[1:],s2,out_+s1[0]):
                    return True
            if s2:
                if dfs_topDown(s1,s2[1:],out_+s2[0]):
                    return True
            memo[out_]=False
            return False
        # return dfs_topDown(s1,s2,"")
        def dfs_bottomUp(s1:str,s2:str,s3:str,n:int,m:int,len_:int,memo={})->bool:
            print(n,m,len_)
            if str(n)+str(m) in memo:
                return memo[str(n)+str(m)]
            if len_==0:return True
            a=b=False
            if n-1>=0 and s1[n-1]==s3[len_-1]:
                a=dfs_bottomUp(s1,s2,s3,n-1,m,len_-1)
            if m-1>=0 and s2[m-1]==s3[len_-1]:
                b=dfs_bottomUp(s1,s2,s3,n,m-1,len_-1)

            memo[str(n)+str(m)]=a or b
            return a or b
            
        return dfs_bottomUp(s1,s2,s3,len(s1),len(s2),len(s3))
            
                
                
                
    
                
            
            
    
    
sol=Solution()

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

# s1 = "aab"
# s2 = "d"
# s3 = "aadb"

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"

# s1 = ""
# s2 = ""
# s3 = ""
print(sol.isInterleave(s1,s2,s3))            