list=[2,33,34,56,58,87,89,97]


n=int(input("Enter the number that you have to search in tha list :"))



def search(l,r,list,n):
    mid=r+l//2
    flag=0

    if (n==list[mid]):
        flag=1
        return flag

    while(l<r):
        if (n<list[mid]):
            return search(l,mid - 1,list,n)
        else:
            return search(mid+1,r,list,n)

    else:
        flag=0

    if(flag==1):
        return ("Found...!")
    else:
        return ("Not Found..!")

l=0
r=len(list)-1
print(search(l,r,list,n))

