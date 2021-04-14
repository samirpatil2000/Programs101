def reverseVowe(s):
    i=0
    j=len(s)-1
    s=[str_ for str_ in s]
    vowels=['a','e','i','o','u','A','E','I','O','U']
    print(s)
    while(i<j):
        if s[i] not in vowels:
            i+=1
        if(s[j] not in vowels):
            j-=1
        if(i!=j and s[i] in vowels and s[j] in vowels):
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1
        print(s)
    new=""
    for i in s:
        new+=i
    return new

str="..a."
print(reverseVowe(str))
"......a....."
".....a......"