new_st=[]
min_st=[]


def func(st):
    while(len(st)>0):
        temp=st.pop()
        new_st.append(temp)
        if(len(min_st)==0 or temp<min_st[len(min_st)-1]):
            min_st.append(temp)
        elif(temp>=min_st[len(min_st)-1]):
            min_st.append(min_st[len(min_st)-1])


st_=[18 ,19, 29, 15, 16]
func(st_)
print(new_st,"\n",min_st)


            
            
    