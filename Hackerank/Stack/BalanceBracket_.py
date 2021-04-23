def isBalanced(s):
    st=[]
    i=0
    while(i<len(s)):
        while s[i]=='{' or s[i]=='[' or s[i]=='(':
            st.append(s[i])
            i+=1
        if s[i]=='}' or s[i]==']' or s[i]==')':
            if len(st)==0:
                return "NO"
            else:
                temp=st.pop()
                if s[i]=='}' and (temp=='[' or temp=='('):
                    return "NO"
                elif s[i]==']' and (temp=='{' or temp=='('):
                    return "NO"
                elif s[i]==')' and (temp=='{' or temp=='['):
                    return "NO"
        i+=1
    if len(st)!=0:
        return "NO"
    return "YES"
s="}([[{)[]))]{){}["
print(isBalanced(s))
