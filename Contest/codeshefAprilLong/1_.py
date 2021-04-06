import sys
from sys import stdin,stdout


# list=[i.replace("'","") for i in list]



try:
    def get_ints(): 
        return list(map(int, sys.stdin.readline().strip().split()))
    
    Arr = get_ints()

    def validPair(arr):
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if(arr[i]==arr[j]):
                    print("Yes")
                    return
        print("No")
        return

    validPair(Arr)
except:
    pass