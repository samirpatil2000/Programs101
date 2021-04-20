

def minimumNumber(n,password):
    #num,lo,up,spe
    arr=[0,0,0,0]
    # if(n<6):
    #     return 6-n
    for i in range(n):
        if(password[i].isalpha() and password[i].isupper()):
            arr[2]+=1
        elif(password[i].isalpha() and password[i].islower()):
            arr[1]+=1
        elif(password[i].isnumeric()):
            arr[0]+=1
        else:
            arr[3]+=1
    
    count=0
    sum=0
    for i in arr:
        if(i==0):
            count+=1
        sum+=i
    # if(sum):
    #     return n-sum
    return max(count,6-sum)
            

# psa="sa"

# print(psa[0].isnumeric)
pass_="#Hackerrank1"
print(minimumNumber(len(pass_),pass_))