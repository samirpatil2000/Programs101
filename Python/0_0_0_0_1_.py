class Solution:
    def Quetion_1(self,arr):
        num2=len(arr)-1
        return sum(arr)-(num2*(num2+1))/2
    def Quetion_2(self,):
        return
    def Quetion_3(self,):
        return
    
sol=Solution()
arr=[1,2,3,4,5,5,6]
print(sol.Quetion_1(arr))


A=[1,2,3]
B=[4,5,6]
A.extend(B)
print(A)

A=(1,2,3)
B=(4,5,6)


# Print All elements from A and B
# "Opt 1"={
#     'A.extend(B) Print(A)'
#     'C=A+B Print(C)'
#     'A.append(B) Print(A)'
#     'B.extend(A) Print(B)'
# }
# c=A+B
# print(c)
# x,*y=A
# print(x,y)
# print(*A)

# #  0 1 2 3 4 5
# A=[1,2,4,5,6,3]
# n=len(A)


# print(A[0])
# 5 


# # 1 2 4 5 6 
# {1,2,4,5,6}
# {
#     'key':"sam",
#     2:2,
# }

# b=set(A)
# b[2]

# # """
# A=[1,2,4,5,6]
# B=set(A)


# Time complexity of accessing 2 from the B is

# O(n)
# O(1)
# same as A

# """

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        

        
Dog("Rio",20)

Dog.__init__("Rio",20)

Dog.create("Rio",20)



