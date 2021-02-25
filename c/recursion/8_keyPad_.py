

code_arr=['!|','abc' ,'def', 'ghi','jkl', 'mno', 'pqr', 'stuv', 'wxyz','_']

def getkeyPadCombination(str):
    if(len(str)==0):
        return " "
    ch=str[0]
    rem=str[1:]
    m_list=[]
    recu_result=getkeyPadCombination(rem)
    # print(recu_result)
    for i in code_arr[int(ch)]:
        for j in recu_result:
            m_list.append(i+j)        
    return m_list

print(getkeyPadCombination("24"))