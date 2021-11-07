def findIndex(s,start):
    st=1
    for i in range(start,len(s)):
        if s[i]=="(":
            st+=1
        elif s[i]==")":
            st-=1
            if st==0:
                return i
    return -1
		
def expandedString(s,start,end):
	# Write your code here
    result=""
    i=start
    while i<end:
     if s[i]=="(":
        idx=findIndex(s,i+1)
        x=expandedString(s,i+1,idx)
        
        result+=(x)*(int(s[idx+2]))
        prev_i=i
        i=(idx+4)
        print(x,idx,i,result,prev_i)
     elif s[i]!=")":
        result+=s[i]
        print(result,i,s[i])
        i+=1
    
    return result
s="(ab){3}(cd){2}"
s="(ab(c){3}d){2}"
print(expandedString(s,0,len(s)))