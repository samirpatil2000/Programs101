def checkValidString(s):
    count=0
    wild_card=0
    for i in range(len(s)):
        if(s[i]=='('):
            count+=1
        elif(s[i]==')'):
            count-=1
        else:
            wild_card+=1
    if(count==0):
        return True
    else:
        if(count>0 and count-wild_card==0):
            return True
        elif(count<0 and count+wild_card==0):
            return True
        else:
            return False


s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
s_="((*()*(*)))(*)()"
print(checkValidString(s_))
            