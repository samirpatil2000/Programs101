list1=[]
#
for i in range(0,100):
    if i%3==0:
        list1.append(i)
    i+=1
print(list1)
list2=list1
# list2.extend(list1)
# print(list2)




# count=1
# i=0
# while count<=40:
#     if i%3==0:
#         list1.append(i)
#         count+=1
#     i+=1
# print(list1)


# Now remove the first occurrences of number 21 from the list
# def remove_list(list,v):
#     for i in list:
#         if i==v:
#             list.remove(v)
#             break
#     return print(list)
#
# remove_list(list2,9)



# find element from the list
#
# def find_element(list,v):
#     (found,i)=(False,0)
    # pos=-1
    # for i in list:
    #     if i==v:
    #         (found,pos)=(True,list.index(i))
    # if not found:
    #     pos=-1
    #
    # return print(pos)

    #using while loop
#     while i <len(list):
#         if list[i]==v:
#             (found,pos)=(True,list.index(i))
#
#     if not found:
#         pos=-1
#     return print(pos)
#
#
# find_element(list1,9)

# find the number is in the element in the list or not

def find_number(list,v,l,r):    # This function is work if you know the index of l r
    mid= (l+r)//2
    if (r - l ==0 ):
        return False
    if (v==list[mid]):
        return True
    elif (v < list[mid]):
        return find_number(list,v,l,mid)
    elif (v > list[mid]):
        return find_number(list,v,mid+1,r)
    else:
        return False

print(find_number(list1,79,25,33))

# With the number

# def find_number_1(list,v,l,r):










