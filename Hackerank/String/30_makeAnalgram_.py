
def analgram(s1,s2):
    
    dict_1={char:(s1.count(char)) for char in s1}
    dict_2={char:(s2.count(char)) for char in s2}
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
                dict_2[key]=abs(dict_2[key]-dict_1[key])
                dict_1[key]=0
            else:
                dict_1[key]=abs(dict_1[key]-dict_2[key])
                dict_2[key]=0
                
    for val in dict_2.values():
        count+=(val)
    for val in dict_1.values():
        count+=(val)
    return count

s1,s2="cde","abc"

print(analgram(s1,s2))