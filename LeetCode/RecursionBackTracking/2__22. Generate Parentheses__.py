from typing import List


class Solution:
    def isValid(self,str_):
        st=[]
        for w in str_:
            if not st:
                if w==")":
                    return False
                st.append(w)
            else:
                if st[-1]!=w:
                    st.pop()
                else:
                    st.append(w)
        if st:return False
        return True
    
    def generateParenthesis(self, n: int) -> List[str]:
        set_=set()
        def makePar(str_,i,j):
            for i in range(1,n-1):
                for j in range(i,n-1):
                    if str_[i]=="(":str_[i]=")"
                    else:str_[i]="("
                    if str_[j]=="(":str_[j]=")"
                    else:str_[j]="("
                    
                    if self.isValid(str_):
                        set_.add(''.join(str_))
                        makePar(str_,i,j)
                    else:
                        continue
        ans=[]          
        def backtracking(open_,close_,curr):
            if open_==close_ and open_==0:
                ans.append("".join(curr))
                return
            if open_>0:
                curr.append("(")
                backtracking(open_-1,close_,curr)
                curr.pop()
            if open_<close_:
                curr.append(")")
                backtracking(open_,close_-1,curr)
                curr.pop()

        
                    
                    
        x=''.join(["(" for _ in range(n)])+''.join([")" for _ in range(n)])
        # print(x)
        
        # makePar(list(x),1,2)
        backtracking(n,n,[])
        return ans
        
sol=Solution()
print(sol.generateParenthesis(3))
            