

def reverseStack(str_):
    st=[]
    for i in str_:
        st.append(i)
    result_=""
    while(len(st)>0):
        result_+=st.pop()
    return result_

s="samir"
print(reverseStack(s))