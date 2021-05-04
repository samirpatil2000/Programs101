def marsExploration(s):
    # Write your code here
    count_=0
    for i in range(len(s)):
        x=i
        while(x>=0):
            x-=3
        x+=3
        if x==1 and s[i]!="O":
            count_+=1
        elif (x==0 or x==2) and s[i]!="S":
            count_+=1
        
    return count_
s="OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS"
print(marsExploration(s))