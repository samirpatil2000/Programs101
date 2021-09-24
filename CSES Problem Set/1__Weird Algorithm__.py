def weirdAlgo(n):
    print(n,end=" ")
    while n!=1:
        if n&1==1:
            n*=3
            n+=1
        else:
            n>>=1
        print(n,end=" ")
    print()
    

n=int(input())
weirdAlgo(n)