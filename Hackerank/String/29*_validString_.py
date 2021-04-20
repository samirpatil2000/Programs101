
def validString(s):
    dict_={}
    for i in range(len(s)):
        if s[i] in dict_:
            dict_[s[i]]+=1
        else:
            dict_[s[i]]=1
    
    
    x = list(dict_.values())[0]
    print(dict_,"\n",x)
    count=0
    for key in dict_.keys():
        
        if dict_[key]!=x:
            if (abs(dict_[key]-x)!=1 and count==1) or (abs(dict_[key]-x)==1 and count==1):
                # print("sasa")
                return "NO"
        if abs(dict_[key]-x)==1:
            count+=1
            # print(dict_[key],x,"Pass With Count")/
        elif abs(dict_[key]-x)>1:
            count+=1
            # print("sa")
            # return "NO"
        # print(dict_[key],x,"Pass",abs(dict_[key]-x))
            
        
    return dict_,"YES"


s="abcdefghhgfedecba"
print(validString(s))
        
            
    