from ctypes import pythonapi


def staircase(n):
    # Write your code here
    for i in range(n):
        for j in range(1,n-i):
            print(" ",end="")
        for j in range(n-i,n+1):
            print("#",end="")
        print()
            

staircase(4)

def timeConversion(s):
    # Write your code here
    s=list(s)
    if s[-2]+s[-1]=="AM":
        if s[0]+s[1]=="12":
            s[0]="0"
            s[1]="0"
    else:
        
        if int(s[0]+s[1])<12:
            hr=int(s[0]+s[1])+12
            hr=str(hr)
            s[0]=hr[0]
            s[1]=hr[1]
    return "".join(s)
s="05:01:00PM"
print(timeConversion(s))