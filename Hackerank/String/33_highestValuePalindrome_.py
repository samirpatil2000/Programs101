

def palindrome(n,s,k):
    i=n//2-1
    j=i+2
    if n%2==0:
        i=n//2-1
        j=i+1
        
    
    while(i>=0 and j<n and k>=0):
        if(s[i]!=s[j]):
            s[i]=max(s[i],s[j])
            s[j]=s[i]
            k-=1
        
        
        
    print(i,s[i],s[j],j)

n = 4
k = 1
s = '39543'

palindrome(len(s),s)
    
    

    
    
    