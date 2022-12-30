
k=8
list=[(1,7),(1,5),(19,23)]
sorted_list=sorted(list)
print(sorted_list)
for i in sorted_list:
    l=i[1]-i[0]+1
    if(k<=l):
        print(i[0]+k-1)
        break
    k=k-l;