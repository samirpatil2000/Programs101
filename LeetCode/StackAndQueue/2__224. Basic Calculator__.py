class Solution:
    def calculate(self, s: str) -> int:
        set_=set([str(i) for i in range(0,10)])
        def findIndex(start_idx):
            st=[]
            for i in range(start_idx,len(s)):
                
                if s[i]=="(":
                    st.append(s[i])
                elif s[i]==")":
                    st.pop()
                    if not st:
                        return i
            
            
        def solve(start,end):
            result=0
            i=start
            while i<end:
                if s[i]=="(":
                    index=findIndex(i)
                    result+=solve(start=i+1,end=index)
                elif s[i] in set_:
                    if i>0:
                        if s[i-1]=="(" or s[i-1]==" ":
                            result+=s[i]
                        elif s[i-1]=="-" or s[i-1]=="+":
                            if 
                            
                    
                    