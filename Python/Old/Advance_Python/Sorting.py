list1=[12,45,9,89,43,6,875,43,234,56,676,4]
#selection sort
def selection_sort(list):

    for start in range(len(list)):
        minpos=start
        for i in range(start,len(list)):
            if list[i] < list[minpos]:
                minpos=i

            (list[start],list[minpos]) = (list[minpos],list[start])

    return print(list)

selection_sort(list1)
list1.sort()
print(list1)
list2=[]
for i in range(0,10000):
    j=10000-i
    list2.append(j)
# print(list2)

selection_sort(list2)
# it take lots of time so we implement it
#insertion sort


def insertion_sort(list):
    for slice in range(len(list)):
        pos=slice
        while pos >0 and list[pos]<list[pos-1]:
            (list[pos],list[pos-1])=(list[pos-1],list[pos])
            pos = pos-1
    return print(list)


insertion_sort(list2)
