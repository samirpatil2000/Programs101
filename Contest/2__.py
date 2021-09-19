

# from sys import stdin


# n=int(input())
# list_=[]
# while n:
#     n-=1 #name,num,marks
#     name,num,marks=stdin.readline().split()
#     arr = [str(name),int(num),int(marks)]
#     list_.append(arr)
    

# def fun(list_):
#     list_.sort(key=lambda x:(-x[2],x[0],x[1]))
#     return list_
# for i in fun(list_):
    
#     print(i[0],i[1],i[2])



"""3
samir 1 34
abc 2 35
adb 1 35"""
"""
6
ajay 7 27
ajeet 2 22
suraj 5 20
sachin 11 18
rahul 12 14
rohit 18 18"""

def fun(n:int):
    x=1
    count_=0
    while n>0:
        if n==x:
            n-=x
            count_+=1
            break
        n-=2*x
        count_+=2
        if n>x:
            x+=1
        elif n<x:
            x-=1
    return count_

# t=int(input())
# while t:
#     t-=1
#     n=int(input())
#     print(fun(n))
        
    
"""
3
4
1
9
"""

# n=input()
# k=int(input())

# def fun(n,k):
#     if len(n)==k:
#         print("True ",len(n))
#     else:
#         print("False ",len(n))
# fun(n,k)

s=input()

def fun(s):
    n=len(s)
    i=0
    res=0
    while i<n:
        count=1
        while i+1<n and s[i]==s[i+1]:
            i+=1
            count+=1  
        if count%2==0:
            res+=count
        i+=1
    return res

print(fun(s))