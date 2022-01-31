# def


def merge(A,B):
    C=[]
    (m,n)=(len(A),len(B))
    (i,j)=(0,0)
    while (i+j < m+n):
        if j == n:  #B is empty
            C.append(A[i])
            i = i + 1
        elif i == m:
            C.append(B[j])
            j = j + 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i=i+1
        elif A[i] > B[j]:
            C.append(B[j])
            j=j+1
    return C
# L=[]
# R=[]
# for i in range(0,50):
#     L.append(i)
# for i in range(0,50):
#     R.append(i*2)
# print(L ,R)
# L=list(range(0,1000,2))
# R=list(range(1,978,2))
#

list1=list(range(100000,0,-2))

def mergesort(list,left,right):
    if right-left <= 1:
        return list[left:right]
    if right-left >1 :
        mid=(left+right)// 2
        L=mergesort(list,left,mid)
        R=mergesort(list,mid,right)
        return merge(L,R)

print(mergesort(list1,0,len(list1)))