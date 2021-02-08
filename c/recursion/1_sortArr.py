
arr=[1,0,5,2,4,7]

print(arr)


def insertElement(list,temp):
    if(len(list)==0 or list[len(list)-1]<=temp):
        list.append(temp)
        return
    val=list[len(list)-1]
    list.pop()
    insertElement(list,temp)
        

def sortArray(list):
    if len(list)==0:
        return
    # seperating last element
    temp=list[len(list)-1]
    list.pop()
    sortArray(list)
    insertElement(list,temp)

sortArray(arr)
print(arr)

    