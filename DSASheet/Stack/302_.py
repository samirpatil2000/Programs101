

def paranthesisChecker(str_):
    st=[]
    i=0
    while(i<len(str_)):
        if(str_[i]=="{" or str_[i]=="[" or str_[i]=="("):
            st.append(str_[i])
        if(str_[i]=="}" or str_[i]=="]" or str_[i]==")"):
            if(len(st)==0):
                return False
            else:
                temp=st.pop()
                if(str_[i]=='}' and (temp=='[' or temp=='(')):
                    return False
                elif(str_[i]==']' and (temp=='{' or temp=='(')):
                    return False
                elif(str_[i]==')' and (temp=='{' or temp=='[')):
                    return False
        i+=1
    if(len(st)!=0):
        return False
    
    return True

s="{([()])}"
print(paranthesisChecker(s))
            
        