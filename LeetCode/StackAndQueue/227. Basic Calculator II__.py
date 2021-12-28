class Solution:
    def calculate(self, s: str) -> int:
        st=[]
        prev_sign='+'
        no=0
        for i in range(len(s)):
            if s[i].isnumeric():
                no=no*10+int(s[i])
            if (s[i] in ('+','-','/','*') or i==len(s)-1):
                if prev_sign=="+":
                    st.append(no)
                elif prev_sign=="-":
                    st.append(-no)
                elif prev_sign=="*":
                    st.append(st.pop()*no)
                else:
                    st.append(st.pop()/no)
                no=0
                prev_sign=s[i]
        result=0
        while st:
            result+=st.pop()
        import math
        return math.ceil(result)
    
sol=Solution()
s="3+2*2"
s="14-3/2"
print(sol.calculate(s))