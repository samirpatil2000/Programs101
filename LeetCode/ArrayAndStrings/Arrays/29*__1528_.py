def restore(s,indices):
    list=[]
    for s_,i in zip(s,indices):
        list.append([i,s_])
    list=sorted(list)
    # print(list)
    str_=""
    for i in range(len(indices)):
        str_+=list[i][1]
    return str_


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
list__=restore(s,indices)
# list__=sorted(list__)
print(list__)
        