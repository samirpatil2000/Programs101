'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def dfs(arr,memo,index=0,num1="",num2=""):
    str_1=str(index)+"-"+str(num1)+"-"+str(num2)
    str_2=str(index)+"-"+str(num2)+"-"+str(num1)

    if str_1 in memo:
        return memo[str_1]
    elif str_2 in memo:
        return memo[str_2]

    if index==len(arr):
        if num1!="" and num2!="":
            return int(num1)+int(num2)
        return 2**32 
    sum_=min(dfs(arr,memo,index+1,num1+str(arr[index]),num2),
            dfs(arr,memo,index+1,num1,num2+str(arr[index]))
            )
    memo[str_1]=sum_
    return sum_

t=int(input())
while t:
    t-=1
    n=input()
    n=[int(i) for i in n]
    n.sort()
    memo={}
    print(dfs(n,memo=memo))

