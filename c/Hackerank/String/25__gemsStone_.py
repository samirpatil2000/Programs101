
def listChecker(arr_,val):
    # print(arr_)
    for i in range(len(arr_)):
        print(arr_)
        if arr_[i]!="#" and val==arr_[i]:
            arr_[i]="#"
            return True
    return False

def GemsStone(arr_):
    arr_=[list(i) for i in arr_]
    temp=arr_[0]
    count=0
    for ele in temp:
        j=1
        while(j<len(arr_) and listChecker(arr_[j],ele)==True):
            j+=1
        if(j==len(arr_)):
            print(ele,arr_[j-1])
            count+=1
    return count
                
                
            



arr = ['abcdde', 'baccd', 'eeabg']
# arr=['abc','abc','abc']

print(arr)


print(GemsStone(arr))

