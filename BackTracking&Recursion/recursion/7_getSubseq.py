
def getSubSequesnce(str):
    rec_list=[]
    m_list=[]
    if(len(str) == 0):
        return " "
    ch=str[0]
    list=str[1:]
    rec_list=getSubSequesnce(list)
    for i in rec_list:
        m_list.append("_"+i)
        m_list.append(ch+i)
        # print(m_list)
    return m_list

print(getSubSequesnce("ABC"))
