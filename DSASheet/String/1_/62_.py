def countAndSay(n):
    if n==1:
        return "1"
    elif(n==2):
        return "11";
    
    else:
        i=0
        a=countAndSay(n-1)
        b=""
        while(i<len(a)):
            count=1
            c=a[i]
            while(i<len(a)-1 and a[i]==a[i+1]):
                count+=1
                i+=1
            b=b+str(count)+c
            i+=1
        return b

print(countAndSay(4))