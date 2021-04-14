
def calPoints(ops):
    st=[]
    for i in ops:
        if(i=='D'):
            st.append((st[len(st)-1])*2)
        elif(i=='C'):
            st.pop()
        elif(i=='+'):
            st.append((st[len(st)-1]+st[len(st)-2]))
        else:
            st.append(int(i))
    return sum(st)


ops = ["1"]
print(calPoints(ops))