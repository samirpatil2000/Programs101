

def palindrome(n,s,k):
    i=n//2-1
    j=i+2
    if n%2==0:
        i=n//2-1
        j=i+1
        
    
    while(i>=0 and j<n and k>0):
        print(s,k)
        # print(i,s[i],s[j],j)
        if(s[i]!=s[j] and k>=2 and i==0 and int(s[i])<9):
            s[i]=9
            s[j]=s[i]
            k-=2
        
        if(s[i]!=s[j]):
            s[i]=str(max(int(s[i]),int(s[j])))
            s[j]=s[i]
            k-=1
        i-=1
        j+=1
    print(s,k)
    i=0
    j=n-1
    while(i<=j):
        print(s[i],s[j],k)
        if(int(s[i])<9 and s[i]==s[j] and k>=2):
            print("A")
            s[i]=str(9)
            s[j]=str(9)
            k-=2
        if(s[i]!=s[j] and k<=0):
            print(-1)
            return -1
        i+=1
        j-=1
    if n%2!=0 and k>0 and int(s[n//2])!=9:
        s[n//2]=str(9)
        
            
    str_=""
    for i in s:
        str_+=str(i)
    
    print(int(str_))
        
    
        
        

k = 1
s = '12321'

# print(s[len(s)//2])
palindrome(len(s),list(s),k)
    
    

    
    
    