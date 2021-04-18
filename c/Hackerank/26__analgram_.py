
def analgram(s):
    if len(s)%2!=0:
        return -1
    
    
    print(sorted(s[:len(s)//2]))
    print(sorted(s[len(s)//2:]))
    dict_1={char:(s[:len(s)//2].count(char)) for char in s[:len(s)//2]}
    dict_2={char:(s[len(s)//2:].count(char)) for char in s[len(s)//2:]}
    print(dict_1,"\n",dict_2)
    count=0
    for key,value in dict_2.items():
        # print(key)
        if key in dict_1:
            if value!=dict_1[key]:
                count+=abs(dict_1[key]-value)
        else:
            count+=value
    return count

s="fdhlvosfpafhalll"
print(analgram(s))