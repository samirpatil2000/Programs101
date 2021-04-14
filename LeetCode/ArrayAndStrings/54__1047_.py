
def removeDuplicates(str_):
    st=[]
    for i in str_:
        if(len(st)!=0):
            if(st[len(st)-1]==i):
                st.pop()
            else:
                st.append(i)
        else:
            st.append(i)
    
    return_str=""
    # st.reverse()
    while(len(st)!=0):
        return_str+=st.pop(0)
    
    return return_str


s="abbaca"
print(removeDuplicates(s))
                    
        