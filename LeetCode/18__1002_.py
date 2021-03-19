
# def checker()

def commanClass(A):
    A=[[str(o) for o in A[m]] for m in range(len(A))]
    str_=A[0]
    return_list=[]
    for i in str_:
        j=1
        count=0
        while(j<len(A)):
            k=0
            while(k<len(A[j])):
                if(A[j][k]!="#" and i==A[j][k]):
                    A[j][k]="#"
                    count+=1
                    break
                k+=1
            # if(count==0):
            #     break
            j+=1
        print(i,A)
        print(count ,len(A))
        if(count==len(A)-1):
            return_list.append(i)
    return return_list
A=["cool","lock","cook"]
print(commanClass(A))