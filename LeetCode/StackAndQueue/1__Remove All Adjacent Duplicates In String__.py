class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if len(st)>0 and st[-1]==s[i]:
                st.pop()
            else:
                st.append(s[i])
        return "".join(st)
    
sol=Solution()
s = "abbaca"
s=""
print(sol.removeDuplicates(s))
                