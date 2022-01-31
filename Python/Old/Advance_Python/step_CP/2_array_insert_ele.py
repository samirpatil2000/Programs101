
list=[2,4,5,7,8,10,14,15,19,23,25]

"""INSERT ELEMENT IN ARRAY"""

def insertElement(position,value,list):
    i=len(list)-1
    while(i>=position):
        list[i+1]=list[i]
        i=-1

    list[position]=value
    return list

print(insertElement(5,100,list))










