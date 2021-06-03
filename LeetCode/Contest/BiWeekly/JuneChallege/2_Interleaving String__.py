class Solution():
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        k,i,j=0,0,0
        if len(s3)!=len(s1)+len(s2):
            return False
        while (k<len(s3) or i<len(s1) or j<len(s2)):
            if i<len(s1) and s3[k]==s1[i]:
                k+=1
                i+=1
            elif j<len(s2) and s3[k]==s2[j]:
                k+=1
                j+=1
            else:
                return False
        return True

sol=Solution()
s1 = "a"
s2 = ""
s3 = "c"
print(sol.isInterleave(s1,s2,s3))