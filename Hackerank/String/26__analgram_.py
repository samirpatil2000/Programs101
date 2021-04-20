
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
            # dict_1[key]=
            if dict_1[key]==dict_2[key]:
                dict_1[key]=0
                dict_2[key]=0
            elif dict_1[key]<dict_2[key]:
                dict_2[key]=dict_2[key]-dict_1[key]
                dict_1[key]=0
            else:
                dict_1[key]=dict_1[key]-dict_2[key]
                dict_2[key]=0
                
    for val in dict_2.values():
        count+=val
    return count

s="fdhlvosfpafhalll"
print(analgram(s))