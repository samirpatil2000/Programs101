#Find the lenght of list
import sys
sys.setrecursionlimit(20000)
list1=[]
for i in range(0,9999):
    list1.append(i)
print(list1)
# print(len(list1))

def find_length(list):
    if list==[]:
        return 0
    else:
        return (1+find_length(list[1:]))

print(find_length(list1))

#gcd using recurssive method




