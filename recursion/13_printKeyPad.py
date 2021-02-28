

code_arr=['!|','abc' ,'def', 'ghi','jkl', 'mno', 'pqr', 'stuv', 'wxyz','_']

def printkeyPadCombination(str,output):
    if(len(str)==0):
        print(output)
        return
    ch=str[0]
    rem=str[1:]
    for i in code_arr[int(ch)]:
        printkeyPadCombination(rem,output+i)

printkeyPadCombination("24","")