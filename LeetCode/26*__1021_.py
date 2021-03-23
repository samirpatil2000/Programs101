
def removeOuterParentheses(s):
    st=[]
    str_=""
    for i in range(len(s)):
        if(len(st)==0):
            st.append(s[i])
        elif(len(st)==1):
            if(s[i]==")"):
                st.pop()            
            else:
                st.append(s[i])
                str_+=s[i]
        else:
            if(s[i]=='('):
                str_+=s[i]
                st.append(s[i])
            elif(s[i]==')'):
                str_+=s[i]
                st.pop()
    return str_

S="(()(()))"
S_="(()())(())"
 
def withoutUsingStack(S):
    count=0
    result=""
    for i in S:
        if(i=="("):
            count+=1
            if(count>1):
                result+="("
        else:
            count-=1
            if(count>0):
                result+=")"
    return result

print(withoutUsingStack(S))
print(removeOuterParentheses(S))

                
    
